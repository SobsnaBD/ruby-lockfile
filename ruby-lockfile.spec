Summary:	A ruby library for creating NFS safe lockfiles
Name:		ruby-lockfile
Version:	1.4.3
Release:	0.1
License:	Ruby License
Source0:	http://rubyforge.org/frs/download.php/18699/lockfile-%{version}.tgz
# Source0-md5:	54b3ce6a1f5b2ec4c96dfc954b33fa86
Group:		Development/Languages
URL:		http://rubyforge.org/projects/codeforpeople/
BuildRequires:	rpmbuild(macros) >= 1.484
BuildRequires:	ruby >= 1:1.8.6
BuildRequires:	ruby-modules
%{?ruby_mod_ver_requires_eq}
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# nothing to be placed there. we're not noarch only because of ruby packaging
%define		_enable_debug_packages	0

%description
A ruby library for creating NFS safe lockfiles.

%package rdoc
Summary:	Documentation files for ruby-lockfile
Group:		Documentation
Requires:	ruby >= 1:1.8.7-4

%description rdoc
Documentation files for ruby-lockfile.

%prep
%setup -q -n lockfile-%{version}

%build
rdoc --ri --op ri lib
rdoc --op rdoc lib
rm -f ri/created.rid

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_rubylibdir},%{ruby_ridir},%{ruby_rdocdir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_rubylibdir}
cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}
cp -a rdoc $RPM_BUILD_ROOT%{ruby_rdocdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{ruby_rubylibdir}

%files rdoc
%defattr(644,root,root,755)
%{ruby_rdocdir}/%{name}-%{version}
%{ruby_ridir}
