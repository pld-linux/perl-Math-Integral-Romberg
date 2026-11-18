#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Math
%define		pnam	Integral-Romberg
Summary:	Math::Integral::Romberg - scalar numerical integration
Summary(pl.UTF-8):	Math::Integral::Romberg - całkowanie numeryczne
Name:		perl-Math-Integral-Romberg
Version:	0.04
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/authors/id/B/BO/BOESCH/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d74535fdbf43c700e457cae6d12f5663
URL:		http://search.cpan.org/dist/Math-Integral-Romberg/
BuildRequires:	perl-Module-Build
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Math::Integral::Romberg module numerically estimates the integral of
function using Romberg integration, a faster relative of Simpson's
method.

%description -l pl.UTF-8
Moduł Math::Integral::Romberg numerycznie przybliża wartość całki
funkcji przy użyciu całkowania Romberga, szybszego niż metoda
Simpsona.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	installdirs=vendor \
	destdir=$RPM_BUILD_ROOT
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Changes
%dir %{perl_vendorlib}/Math/Integral
%{perl_vendorlib}/Math/Integral/Romberg.pm
%{_mandir}/man3/*
