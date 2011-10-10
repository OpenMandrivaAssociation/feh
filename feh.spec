Summary:        Image viewer at heart, though it does other cool stuff
Name:           feh
Version:        2.0
Release:        %mkrel 1
License:        MIT
Group:          Graphics
URL:            https://derf.homelinux.org/projects/feh/

Source0:        https://derf.homelinux.org/projects/feh/%{name}-%{version}.tar.bz2
Source1:        %{name}-icons.tar.bz2

BuildRoot:      %{_tmppath}/%{name}-buildroot
Buildrequires:  imlib2-devel libxt-devel libxinerama-devel
Buildrequires:  giblib-devel
Buildrequires:  jpeg-devel 
BuildRequires:  png-devel
BuildRequires:  curl-devel

%description
Feh is an image viewer, but it does a whole lot of other cool stuff as
well. There are simply too many to mention them here so please check the
docs/homepage.


%prep
%setup -q
%setup -q -T -D -a1

%build
%setup_compile_flags
%make PREFIX=/usr

%install
%__rm -rf %{buildroot}
%makeinstall_std PREFIX=%{_prefix}

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=%{name}
Comment=%{summary}
Exec=%{name} -c
Icon=%{name}
Terminal=false
Type=Application
Categories=X-MandrivaLinux-Multimedia-Graphics;
EOF


%__install -D -m 644 %{name}-48.png %{buildroot}%{_liconsdir}/%{name}.png
%__install -D -m 644 %{name}-32.png %{buildroot}%{_iconsdir}/%{name}.png
%__install -D -m 644 %{name}-16.png %{buildroot}%{_miconsdir}/%{name}.png


%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

#let files section handle docs
rm -rf %{buildroot}%{_docdir}%{name}

%clean
%__rm -rf %{buildroot}


%files
%defattr(0755,root,root,0755)
%{_bindir}/*
%defattr(0644,root,root,0755)
%doc AUTHORS ChangeLog README TODO examples
%{_datadir}/%{name}/fonts/*
%{_datadir}/%{name}/images/*
%{_mandir}/man1/*
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_datadir}/applications/*


