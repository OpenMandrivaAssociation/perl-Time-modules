%define version 2006.0814

Summary:	Time modules for perl
Name:		perl-Time-modules
Version:	%{version}
Release:	%mkrel 4
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
rm -rf $RPM_BUILD_ROOT
%{__make} PREFIX=$RPM_BUILD_ROOT%{_prefix} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README MANIFEST CHANGELOG
%{_mandir}/*/*
%{perl_vendorlib}/Time/*


