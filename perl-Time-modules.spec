%define version 2011.0517

Summary:	Time modules for perl
Name:		perl-Time-modules
Version:	%{version}
Release:	%mkrel 3
License:	distributable
Group:		Development/Perl
Source:		Time-modules-%{version}.tar.bz2
URL:		http://www.cpan.org/modules/by-module/Time/
Requires:	perl
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
BuildRequires:	perl-devel >= 5.8.0
BuildArch:	noarch

%description
This package contains the following perl5 modules:

        Time::CTime.pm
                ctime, strftime, and asctime
        Time::JulianDay.pm
                Julian Day conversions
        Time::ParseDate.pm
                Reverses strftime and also understands relative times
        Time::Timezone.pm
        Time::DaysInMonth.pm

%prep
%setup -q -n Time-modules-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor PREFIX=%{_prefix}
%{__make}

%install
rm -rf %{buildroot}
%{__make} PREFIX=%{buildroot}%{_prefix} install

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README MANIFEST CHANGELOG
%{_mandir}/*/*
%{perl_vendorlib}/Time/*


