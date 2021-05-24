#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-autobox
Version  : 3.0.1
Release  : 18
URL      : https://cpan.metacpan.org/authors/id/C/CH/CHOCOLATE/autobox-v3.0.1.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/C/CH/CHOCOLATE/autobox-v3.0.1.tar.gz
Summary  : 'call methods on native types'
Group    : Development/Tools
License  : Artistic-2.0
Requires: perl-autobox-license = %{version}-%{release}
Requires: perl-autobox-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(IPC::System::Simple)
BuildRequires : perl(Scope::Guard)
BuildRequires : perl(Test::Fatal)
BuildRequires : perl(Try::Tiny)

%description
autobox version 3.0.1
====================
The autobox pragma allows methods to be called on integers, floats, strings, arrays, hashes, and code references in exactly the same manner as blessed references.

%package dev
Summary: dev components for the perl-autobox package.
Group: Development
Provides: perl-autobox-devel = %{version}-%{release}
Requires: perl-autobox = %{version}-%{release}

%description dev
dev components for the perl-autobox package.


%package license
Summary: license components for the perl-autobox package.
Group: Default

%description license
license components for the perl-autobox package.


%package perl
Summary: perl components for the perl-autobox package.
Group: Default
Requires: perl-autobox = %{version}-%{release}

%description perl
perl components for the perl-autobox package.


%prep
%setup -q -n autobox-v3.0.1
cd %{_builddir}/autobox-v3.0.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-autobox
cp %{_builddir}/autobox-v3.0.1/LICENSE.md %{buildroot}/usr/share/package-licenses/perl-autobox/ce7ac86035018a3588a651c30f7635010f2a69c4
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/autobox.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-autobox/ce7ac86035018a3588a651c30f7635010f2a69c4

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/autobox/autobox.so
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/autobox.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/autobox.pod
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/autobox/universal.pm
