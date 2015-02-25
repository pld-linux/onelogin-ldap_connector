# TODO
# - system jruby?
# - system libs?
Summary:	Onelogin Directory Integration
Name:		onelogin-ldap_connector
Version:	1.25
Release:	0.2
License:	?
# Forever free account can be obtained from https://www.onelogin.com/signup
Source0:	https://s3.amazonaws.com/onelogin-downloads/ldapc/1_25/ldap_connector.zip
# NoSource0-md5:	32d0949fba09e8377535768f8b570575
NoSource:	0
Group:		Libraries
URL:		https://www.onelogin.com/product/directory
Requires:	jre
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir	%{_prefix}/lib/%{name}

%description
OneLogin allows you to synchronize users with any number of
directories, such as Active Directory, LDAP or Google Apps. Import
custom user attributes and pass them on to downstream apps via SAML or
API-based provisioning. The integration with Active Directory
synchronizes users in real-time and supports multiple forests and
domains via a single connector.

%prep
%setup -qc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_appdir},/var/log/ol-ldapc}
cp -a ldap-connector.jar lib resources $RPM_BUILD_ROOT%{_appdir}
ln -s /var/log/ol-ldapc $RPM_BUILD_ROOT%{_appdir}/log

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
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

%dir /var/log/ol-ldapc
