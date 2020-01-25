#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	ExtUtils
%define		pnam	Typemaps-Default
Summary:	ExtUtils::Typemaps::Default - A set of useful typemaps
Name:		perl-ExtUtils-Typemaps-Default
Version:	1.05
Release:	1
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/ExtUtils/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	346c127faf7b74bc4cfc29fa3e8e6f8d
URL:		http://search.cpan.org/dist/ExtUtils-Typemaps-Default/
BuildRequires:	perl-Module-Build
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ExtUtils::Typemaps::Default is an ExtUtils::Typemaps
subclass that provides a set of default mappings (in addition to what
perl itself provides). These default mappings are currently defined
as the combination of the mappings provided by the
following typemap classes which are provided in this distribution:

ExtUtils::Typemaps::ObjectMap, ExtUtils::Typemaps::STL,
ExtUtils::Typemaps::Basic

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/ExtUtils/Typemap/*
%{perl_vendorlib}/ExtUtils/Typemaps
%{_mandir}/man3/*
