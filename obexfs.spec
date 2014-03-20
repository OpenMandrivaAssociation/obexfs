Summary:	FUSE based filesystem using ObexFTP
Name:		obexfs
Version:	0.12
Release:	2
License:	GPLv2+
Group:		Communications
Url:		http://triq.net/obex/
Source0:	http://triq.net/obexfs/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(fuse)
BuildRequires:	pkgconfig(obexftp)

%description
The ObexFS driver is a wrapper for ObexFTP to provide filesystem access
to mobile phones.

%files
%doc AUTHORS COPYING ChangeLog README
%{_bindir}/obexautofs
%{_bindir}/obexfs

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

