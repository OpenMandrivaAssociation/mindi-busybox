%define _enable_debug_packages %{nil}
%define debug_package %{nil}

Summary:	Busybox version suited for Mindi
Name:		mindi-busybox
Version:	1.18.5
Release:	3
License:	GPLv2+
Group:		Archiving/Backup
Url:		https://www.mondorescue.org
Source0:	ftp://ftp.mondorescue.org/src/%{name}-%{version}.tar.gz

%description
This package provides a busybox version suited for Mindi.

%files
%doc ChangeLog LICENSE AUTHORS README TODO NEWS
%{_libdir}/mindi/*

#----------------------------------------------------------------------------

%prep
%setup -q

%build
make oldconfig
make busybox

%install
DESTDIR=%{buildroot}%{_libdir}/mindi/rootfs
make CONFIG_PREFIX=$DESTDIR install


