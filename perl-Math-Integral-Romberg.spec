#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Math
%define		pnam	Integral-Romberg
Summary:	Math::Integral::Romberg - scalar numerical integration
Summary(pl):	Math::Integral::Romberg - ca³kowanie numeryczne
Name:		perl-Math-Integral-Romberg
Version:	0.02
Release:	2
License:	GPL/Artistic
Group:		Development/Languages/Perl
%define	sver	%(echo %{version} | tr . _)
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{sver}.tar.gz
# Source0-md5:	932ea744c11f34b5506a14637ef0421a
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Math::Integral::Romberg module numerically estimates the integral of
function using Romberg integration, a faster relative of Simpson's
method.

%description -l pl
Modu³ Math::Integral::Romberg numerycznie przybli¿a warto¶æ ca³ki
funkcji przy u¿yciu ca³kowania Romberga, szybszego ni¿ metoda
Simpsona.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%{!?_without_tests:%{__make} test}

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
