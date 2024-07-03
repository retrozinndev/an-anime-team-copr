
# !!! NEED FIX FOR ICON NAME IN RESOURCES OF REPO !!!

%global srcname an-anime-borb-launcher
%global app_name An Anime Borb Launcher
%define install_dir %{_libdir}/%{app_name}
%define icon_dir %{_datadir}/icons/hicolor/512x512/apps
%define apps_dir %{_datadir}/applications
%define app_id moe.launcher.%{app_name}
%define build_output anime-borb-launcher

# name needs to be the same as package name in copr
Name: anime-borb-launcher
Version: 1.0.1
Release: 1%{?dist}
License: GPLv3
Summary: An Anime Borb Launcher for Linux with automatic patching and telemetry disabling. App is unmaintened!
Url: https://github.com/an-anime-team/%{srcname}
# Sources can be obtained by
# git clone https://github.com/an-anime-team/%{srcname}.git
# cd %{srcname}
# tito build --tgz
Source0: https://github.com/an-anime-team/%{srcname}/archive/refs/tags/%{version}.tar.gz
BuildArch: x86_64

#-- APPLICATION DEPENDENCIES ---------------------------------------------------#
Requires: git
Requires: libcurl
Requires: libadwaita
Requires: gtk4
Requires: glibc

#-- OPTIONAL DEPENDENCIES ------------------------------------------------------#
Suggests: mangohud
Suggests: gamescope
Suggests: gamemode

#-- BUILD DEPENDENCIES ---------------------------------------------------------#
BuildRequires: rust
BuildRequires: cargo
BuildRequires: git
BuildRequires: libcurl
BuildRequires: libadwaita-devel
BuildRequires: gtk4-devel
BuildRequires: glibc
BuildRequires: glib2
BuildRequires: glib2-devel
BuildRequires: p7zip
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: cairo-devel
BuildRequires: gdk-pixbuf2-devel
BuildRequires: pango-devel
BuildRequires: rust-gdk4-devel

%description
The Honkers Railway launcher for Linux with automatic patching and telemetry disabling 

#-- PREP, BUILD & INSTALL -----------------------------------------------------#
%prep
%autosetup

%build
cargo build --release

%install
# copy binary
mkdir -p %{buildroot}%{install_dir}
cp -f target/release/%{build_output} %{buildroot}%{install_dir}
# rename binary
mv %{buildroot}%{install_dir}/%{build_output} %{buildroot}%{install_dir}/%{name}
# copy icon
mkdir -p %{buildroot}%{icon_dir}
cp -f assets/images/%{app_id}.png %{buildroot}%{icon_dir}
# copy desktop file
mkdir -p %{buildroot}%{apps_dir}
cp -f assets/%{name}.desktop %{buildroot}%{apps_dir}

%post
# create link of binary
ln -sf %{install_dir}/%{name} %{_bindir}/%{name}
# apply exec permision to binary
chmod +x %{install_dir}/%{name}

#-- FILES ---------------------------------------------------------------------#
%files
%doc README.md
%license LICENSE
%{install_dir}/*
%{icon_dir}/%{app_id}.png
%{apps_dir}/%{name}.desktop

#-- CHANGELOG -----------------------------------------------------------------#
%changelog