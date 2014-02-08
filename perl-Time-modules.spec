%define version 2011.0517

Summary:	Time modules for perl
Name:		perl-Time-modules
Version:	%{version}
Release:	4
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




%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 2011.0517-3mdv2012.0
+ Revision: 765790
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 2011.0517-2
+ Revision: 764295
- rebuilt for perl-5.14.x

* Sun May 22 2011 Guillaume Rousse <guillomovitch@mandriva.org> 2011.0517-1
+ Revision: 677402
- update to new version 2011.0517

* Sat May 14 2011 Guillaume Rousse <guillomovitch@mandriva.org> 2011.0505-1
+ Revision: 674700
- update to new version 2011.0505

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 2006.0814-5
+ Revision: 667401
- mass rebuild

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 2006.0814-4mdv2011.0
+ Revision: 426598
- rebuild

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 2006.0814-3mdv2009.1
+ Revision: 351700
- rebuild

* Fri Dec 21 2007 Olivier Blin <blino@mandriva.org> 2006.0814-2mdv2009.0
+ Revision: 136362
- restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 2006.0814-2mdv2008.1
+ Revision: 123841
- kill re-definition of %%buildroot on Pixel's request

* Mon Aug 20 2007 Thierry Vignaud <tv@mandriva.org> 2006.0814-2mdv2008.0
+ Revision: 67554
- rebuild

* Wed May 02 2007 Olivier Thauvin <nanardon@mandriva.org> 2006.0814-1mdv2008.0
+ Revision: 20769
- 2006.0814


* Mon Mar 05 2007 Oden Eriksson <oeriksson@mandriva.com> 2003.1126-2mdv2007.0
+ Revision: 133184
- use mkrel

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - Import perl-Time-modules

* Wed May 12 2004 Michael Scherer <misc@mandrake.org> 2003.1126-1mdk
- New release 2003.1126

