all:
	g++ -lm -std=c++0x dynamic_matrix.cpp -o dynamic_matrix

clean: 
	rm -rf dynamic_matrix
