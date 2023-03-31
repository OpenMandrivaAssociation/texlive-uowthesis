Name:		texlive-uowthesis
Version:	19700
Release:	2
Summary:	Document class for dissertations at the University of Wollongong
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/uowthesis
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/uowthesis.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/uowthesis.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A document class for higher degree research theses in
compliance with the specifications of University of Wollongong
(UoW) theses in the "Guidelines for Preparation and Submission
of Higher Degree Research Theses" (March 2006), by the Research
Student Centre, Research & Innovation Division, UoW.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/uowthesis/UoWlogo.eps
%{_texmfdistdir}/tex/latex/uowthesis/UoWlogo.png
%{_texmfdistdir}/tex/latex/uowthesis/UoWthesis.cls
%doc %{_texmfdistdir}/doc/latex/uowthesis/README
%doc %{_texmfdistdir}/doc/latex/uowthesis/myThesisBib.bib
%doc %{_texmfdistdir}/doc/latex/uowthesis/mythesis.pdf
%doc %{_texmfdistdir}/doc/latex/uowthesis/mythesis.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
