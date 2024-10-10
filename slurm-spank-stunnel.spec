Summary: Slurm SPANK plugin for SSH tunneling and port forwarding support
Name: slurm-spank-stunnel
Version: 0.2.5
Release: 1 
License: GPL
Group: System Environment/Base
Source0: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: slurm-devel
Requires: slurm

%description
Slurm SPANK plugin that allows SSH port forwarding between submit and execution
hosts

%prep
%setup -q

%build
%{__cc} -shared -fPIC -o stunnel.so slurm-spank-stunnel.c

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_libdir}
mkdir -p $RPM_BUILD_ROOT%{_libdir}/slurm
mkdir -p $RPM_BUILD_ROOT%{_libexecdir}
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/slurm
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/slurm/plugstack.conf.d
install -m 755 stunnel.so $RPM_BUILD_ROOT%{_libdir}/slurm
install -m 644 plugstack.conf $RPM_BUILD_ROOT%{_sysconfdir}/slurm/plugstack.conf.d/stunnel.conf.example

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_libdir}/slurm/stunnel.so
%config %{_sysconfdir}/slurm/plugstack.conf.d/stunnel.conf.example

%changelog
* Fri Aug 11 2017 Kilian Cavalotti <kilian@stanford.edu>
- Cleanup and simplify build procedure (don't use autotools)
* Mon Nov 17 2014 Aaron Kitzmiller <aaron_kitzmiller@harvard.edu>
- Initial rpmbuild
