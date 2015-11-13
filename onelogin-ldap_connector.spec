# TODO
# - system jruby?
# - system libs?
%define		ver	%(echo %{version} | tr . _)
Summary:	Onelogin Directory Integration
Name:		onelogin-ldap_connector
Version:	1.32
Release:	0.1
License:	?
Group:		Libraries
# Forever free account can be obtained from https://www.onelogin.com/signup
Source0:	https://s3.amazonaws.com/onelogin-downloads/ldapc/%{ver}/ldap_connector.zip?/ldap_connector-%{version}.zip
# NoSource0-md5:	292e3c7b77fe55ab5cc66d321fffb384
NoSource:	0
Source1:	ol-ldapc.init
Source2:	ol-ldapc.sysconfig
URL:		https://www.onelogin.com/product/directory
Requires:	jre
Requires:	rc-scripts >= 0.4.15
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir	%{_prefix}/lib/ol-ldapc

%description
OneLogin allows you to synchronize users with any number of
directories, such as Active Directory, LDAP or Google Apps. Import
custom user attributes and pass them on to downstream apps via SAML or
API-based provisioning. The integration with Active Directory
synchronizes users in real-time and supports multiple forests and
domains via a single connector.

%prep
%setup -qc
mv ldap_connector/* .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_appdir},/var/log/ol-ldapc,/etc/{rc.d/init.d,sysconfig}}
cp -a ldap-connector.jar lib resources $RPM_BUILD_ROOT%{_appdir}
ln -s /var/log/ol-ldapc $RPM_BUILD_ROOT%{_appdir}/log
install -p %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/ol-ldapc
cp -p %{SOURCE2} $RPM_BUILD_ROOT/etc/sysconfig/ol-ldapc

%clean
rm -rf $RPM_BUILD_ROOT

%post
%service ol-ldapc restart

%preun
if [ "$1" = "0" ]; then
	%service -q ol-ldapc stop
fi

%files
%defattr(644,root,root,755)
%doc README
%attr(754,root,root) /etc/rc.d/init.d/ol-ldapc
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/ol-ldapc
%dir %{_appdir}
%{_appdir}/ldap-connector.jar
%dir %{_appdir}/lib
%{_appdir}/log
%dir %{_appdir}/lib/java
%{_appdir}/lib/java/commons-codec-1.6.jar
%{_appdir}/lib/java/commons-io-2.4.jar
%{_appdir}/lib/java/commons-logging-1.1.1.jar
%{_appdir}/lib/java/fluent-hc-4.2.3.jar
%{_appdir}/lib/java/httpclient-4.2.3.jar
%{_appdir}/lib/java/httpclient-cache-4.2.3.jar
%{_appdir}/lib/java/httpcore-4.2.2.jar
%{_appdir}/lib/java/httpmime-4.2.3.jar
%{_appdir}/lib/java/jruby-complete-1.7.1.jar
%dir %{_appdir}/resources
# use ca-certificates instead?
%{_appdir}/resources/cert.crt

%dir %attr(700,root,root) /var/log/ol-ldapc
