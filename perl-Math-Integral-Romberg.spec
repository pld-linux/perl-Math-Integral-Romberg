#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Math
%define		pnam	Integral-Romberg
Summary:	Math::Integral::Romberg - scalar numerical integration
Summary(pl.UTF-8):	Math::Integral::Romberg - całkowanie numeryczne
%define	_ver	%(echo %{version} | tr . _)
Name:		perl-Math-Integral-Romberg
Version:	0.02
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{_ver}.tar.gz
# Source0-md5:	932ea744c11f34b5506a14637ef0421a
URL:		http://search.cpan.org/dist/Math-Integral-Romberg/
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
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Release
%dir %{perl_vendorlib}/Math/Integral
%{perl_vendorlib}/Math/Integral/Romberg.pm
%{_mandir}/man3/*
