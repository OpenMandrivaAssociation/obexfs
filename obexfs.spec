%define name		obexfs
%define version		0.12
%define beta		0
%if %beta
%define release		%mkrel 0.%beta.1
%else
%define release		%mkrel 1
%endif

Name:			%{name}
Summary:		FUSE based filesystem using ObexFTP
Version:		%{version}
Release:		%{release}
License:		GPLv2+
%if %beta
Source0:		http://triq.net/obexfs/%name-%version-%beta.tar.gz
%else
Source0:		http://triq.net/obexfs/%name-%version.tar.gz
%endif
Group:			Communications
URL:			http://triq.net/obex/
BuildRoot:		%{_tmppath}/%{name}-%{version}-root
BuildRequires:		obexftp-devel
BuildRequires:		fuse-devel


%description
The ObexFS driver is a wrapper for ObexFTP to provide filesystem access
to mobile phones.

%prep
%setup -q

%build
%configure
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root, -)
%doc AUTHORS COPYING ChangeLog README
%{_bindir}/obexautofs
%{_bindir}/obexfs
