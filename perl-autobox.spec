#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-autobox
Version  : 3.0.1
Release  : 4
URL      : https://cpan.metacpan.org/authors/id/C/CH/CHOCOLATE/autobox-v3.0.1.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/C/CH/CHOCOLATE/autobox-v3.0.1.tar.gz
Summary  : 'call methods on native types'
Group    : Development/Tools
License  : Artistic-2.0
Requires: perl-autobox-lib = %{version}-%{release}
Requires: perl-autobox-license = %{version}-%{release}
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
Requires: perl-autobox-lib = %{version}-%{release}
Provides: perl-autobox-devel = %{version}-%{release}

%description dev
dev components for the perl-autobox package.


%package lib
Summary: lib components for the perl-autobox package.
Group: Libraries
Requires: perl-autobox-license = %{version}-%{release}

%description lib
lib components for the perl-autobox package.


%package license
Summary: license components for the perl-autobox package.
Group: Default

%description license
license components for the perl-autobox package.


%prep
%setup -q -n autobox-v3.0.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-autobox
cp LICENSE.md %{buildroot}/usr/share/package-licenses/perl-autobox/LICENSE.md
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
/usr/lib/perl5/vendor_perl/5.28.1x86_64-linux-thread-multi/autobox.pm
/usr/lib/perl5/vendor_perl/5.28.1x86_64-linux-thread-multi/autobox.pod
/usr/lib/perl5/vendor_perl/5.28.1x86_64-linux-thread-multi/autobox/universal.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/autobox.3

%files lib
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1x86_64-linux-thread-multi/auto/autobox/autobox.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-autobox/LICENSE.md
