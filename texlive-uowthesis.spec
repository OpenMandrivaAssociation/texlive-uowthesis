# revision 19700
# category Package
# catalog-ctan /macros/latex/contrib/uowthesis
# catalog-date 2010-07-28 12:27:25 +0200
# catalog-license lppl1.3
# catalog-version 1.0a
Name:		texlive-uowthesis
Version:	1.0a
Release:	8
Summary:	Document class for dissertations at the University of Wollongong
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/uowthesis
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/uowthesis.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/uowthesis.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Thu Jan 05 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0a-2
+ Revision: 757323
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.0a-1
+ Revision: 719856
- texlive-uowthesis
- texlive-uowthesis
- texlive-uowthesis

