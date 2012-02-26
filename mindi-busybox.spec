#
# $Id$
#
Summary:	Busybox version suited for Mindi
Name:		mindi-busybox
Version:	1.18.5
Packager:	Bruno Cornec <bcornec@mandriva.org>
Release:	%mkrel 1
License:	GPL
Group:		Archiving/Backup
Url:		http://www.mondorescue.org
Source:		ftp://ftp.mondorescue.org/src/%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(id -u -n)
Buildrequires: gcc
ExcludeArch:	ppc

%description
This package provides a busybox version suited for Mindi.

%prep
%setup -n %name-%{version}

%build
make oldconfig
make busybox

%install
%{__rm}  -rf $RPM_BUILD_ROOT

DESTDIR=${RPM_BUILD_ROOT}%{_libdir}/mindi/rootfs
make CONFIG_PREFIX=$DESTDIR install

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc ChangeLog INSTALL LICENSE AUTHORS README TODO NEWS
%{_libdir}/mindi

%changelog
