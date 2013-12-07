%define version 2011.0517

Summary:	Time modules for perl
Name:		perl-Time-modules
Version:	%{version}
Release:	7
License:	distributable
Group:		Development/Perl
Url:		http://www.cpan.org/modules/by-module/Time/
Source0:	Time-modules-%{version}.tar.bz2
BuildArch:	noarch
BuildRequires:	perl-devel >= 5.8.0
Requires:	perl

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
%setup -qn Time-modules-%{version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor PREFIX=%{_prefix}
%make

%install
%makeinstall_std

%files
%doc README MANIFEST CHANGELOG
%{perl_vendorlib}/Time/*
%{_mandir}/man3/*

