
default: final
#	pdflatex paper.tex

final:

	pdflatex paper.tex
	bibtex paper
	pdflatex paper.tex
	pdflatex paper.tex

clean:
	rm *~ *.aux *.out *.toc *.blg *.bbl *.log *.tdo

diff:
	cp paper.tex paper_new.tex
	hg revert paper.tex
	cp paper.tex paper_old.tex
	cp paper_new.tex paper.tex
	latexdiff paper_old.tex paper.tex > diff.tex
	pdflatex diff.tex
	bibtex diff.aux
	pdflatex diff.tex
	pdflatex diff.tex
