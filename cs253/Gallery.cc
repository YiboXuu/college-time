#include "Gallery.h"
#include "Enemy.h"
#include <iostream>
#include <istream>
#include <vector>
#include <ctype.h>
#include <fstream>
#include <map>
#include <string>
#include <cctype>
#include <iterator>
#include <sstream>
using namespace std;

Gallery::Gallery(const Gallery &rhs){
	count = rhs.count;
	//MyPair = rhs.MyPair;
	//KVpair = rhs.KVpair;
	containers = rhs.containers;
	}
	
Gallery::~Gallery(){
	}

Gallery &Gallery::operator=(const Gallery &rhs) {
	count = rhs.count;
	//MyPair = rhs.MyPair;
   // KVpair = rhs.KVpair;
   containers  =rhs.containers;
    return *this;
}

Gallery::Gallery(const string& f1,const string& f2){
	if(checkLegitKeyfile(f1)){
		if(checkLegitKeyfile(f2))	
			throw  runtime_error("ERROR: contains too many keyfiles.");
		else 
			read(f2,f1);}
	else if(checkLegitKeyfile(f2)){
		read(f1,f2);
		}
	else{
		throw runtime_error("ERROR: no keyfile");
		}
	}

Gallery::Gallery(const string& f1,const string& f2,const string& f3){
	if(checkLegitKeyfile(f1)){
		if(checkLegitKeyfile(f2) || checkLegitKeyfile(f3) )	
			throw  runtime_error("ERROR: contains too many keyfiles.");
		else{
			read(f2,f1);
			read(f3,f1);
			}
				}
	else if(checkLegitKeyfile(f2)){
				if(checkLegitKeyfile(f3) )	
							throw  runtime_error( "ERROR: contains too many keyfiles.");
				else{
						read(f1,f2);
						read(f3,f2);}
		}
	else if(checkLegitKeyfile(f3)){
		read(f1,f3);
		read(f2,f3);
		}
	else{
		throw runtime_error("ERROR: no keyfile");
		}
	}
	
	
Gallery::Gallery(const string& f1,const string& f2,const string& f3,const string& f4){
	if(checkLegitKeyfile(f1)){
		if(checkLegitKeyfile(f2) || checkLegitKeyfile(f3) ||  checkLegitKeyfile(f4))	
			throw  runtime_error("ERROR: contains too many keyfiles.");
		else{
			read(f2,f1);
			read(f3,f1);
			read(f4,f1);
			}
				}
	else if(checkLegitKeyfile(f2)){
				if(checkLegitKeyfile(f3)|| checkLegitKeyfile(f4))	
							throw  runtime_error("ERROR: contains too many keyfiles.");
				else{
						read(f1,f2);
						read(f3,f2);
						read(f4,f2);
						}
		}
	else if(checkLegitKeyfile(f3)){
		if(checkLegitKeyfile(f4))	
							throw  runtime_error("ERROR: contains too many keyfiles.");
				else{
						read(f1,f3);
						read(f2,f3);
						read(f4,f3);
						}
		}
	else if(checkLegitKeyfile(f4)){
		read(f1,f4);
		read(f2,f4);
		read(f3,f4);
		
		}
	else{
		throw runtime_error("ERROR: no keyfile");
		}
	}
	
Gallery::Gallery(const string& f1,const string& f2,const string& f3,const string& f4,const string& f5){
	if(checkLegitKeyfile(f1)){
		if(checkLegitKeyfile(f2) || checkLegitKeyfile(f3) ||  checkLegitKeyfile(f4) ||  checkLegitKeyfile(f5))	
			throw  runtime_error( "ERROR: contains too many keyfiles.");
		else{
			read(f2,f1);
			read(f3,f1);
			read(f4,f1);
			read(f5,f1);
			}
				}
	else if(checkLegitKeyfile(f2)){
				if(checkLegitKeyfile(f3)|| checkLegitKeyfile(f4)||  checkLegitKeyfile(f5))	
							throw  runtime_error("ERROR: contains too many keyfiles.");
				else{
						read(f1,f2);
						read(f3,f2);
						read(f4,f2);
						read(f5,f2);
						}
		}
	else if(checkLegitKeyfile(f3)){
		if(checkLegitKeyfile(f4)||  checkLegitKeyfile(f5))	
							throw  runtime_error("ERROR: contains too many keyfiles.");
				else{
						read(f1,f3);
						read(f2,f3);
						read(f4,f3);
						read(f5,f3);
						}
		}
	else if(checkLegitKeyfile(f4)){
		if(checkLegitKeyfile(f5))	
							throw  runtime_error("ERROR: contains too many keyfiles.");
				else{
						read(f1,f4);
						read(f2,f4);
						read(f4,f4);
						read(f5,f4);
						}
		
		}
	else if(checkLegitKeyfile(f5)){
			read(f1,f5);
			read(f2,f5);
			read(f3,f5);
			read(f4,f5);	
			}
	else{
		throw runtime_error("ERROR: no keyfile");
		}
	}
	
	
Gallery::Gallery(const string& f1,const string& f2,const string& f3,const string& f4,const string& f5,const string& f6){
	if(checkLegitKeyfile(f1)){
		if(checkLegitKeyfile(f2) || checkLegitKeyfile(f3) ||  checkLegitKeyfile(f4) ||  checkLegitKeyfile(f5)||  checkLegitKeyfile(f6))	
							throw  runtime_error( "ERROR: contains too many keyfiles.");
		else{
			read(f2,f1);
			read(f3,f1);
			read(f4,f1);
			read(f5,f1);
			read(f6,f1);
			}
				}
	else if(checkLegitKeyfile(f2)){
				if(checkLegitKeyfile(f3)|| checkLegitKeyfile(f4)||  checkLegitKeyfile(f5) ||  checkLegitKeyfile(f6))	
							throw  runtime_error("ERROR: contains too many keyfiles.");
				else{
						read(f1,f2);
						read(f3,f2);
						read(f4,f2);
						read(f5,f2);
						read(f6,f2);
						}
		}
	else if(checkLegitKeyfile(f3)){
		if(checkLegitKeyfile(f4)||  checkLegitKeyfile(f5) ||  checkLegitKeyfile(f6))	
							throw  runtime_error("ERROR: contains too many keyfiles.");
				else{
						read(f1,f3);
						read(f2,f3);
						read(f4,f3);
						read(f5,f3);
						read(f6,f3);
						}
		}
	else if(checkLegitKeyfile(f4)){
		if(checkLegitKeyfile(f5)||  checkLegitKeyfile(f6))	
							throw  runtime_error("ERROR: contains too many keyfiles.");
				else{
						read(f1,f4);
						read(f2,f4);
						read(f3,f4);
						read(f5,f4);
						read(f6,f4);
						}
		
		}
	else if(checkLegitKeyfile(f5)){
			if(checkLegitKeyfile(f6))	
							throw  runtime_error("ERROR: contains too many keyfiles.");
				else{
						read(f1,f5);
						read(f2,f5);
						read(f3,f5);
						read(f4,f5);
						read(f6,f5);
						}
			}
	else if(checkLegitKeyfile(f6)){
			
				
						read(f1,f6);
						read(f2,f6);
						read(f3,f6);
						read(f4,f6);
						read(f5,f6);
						
			}
	else{
		throw runtime_error("ERROR: no keyfile");
		}
	}
	
bool Gallery::checkLegitKeyfile(string file){ //detect is keyfile or not  
	string Space = " \t\n\f\v"; 
	string Alphabic = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890";
	string input;
	ifstream readK(file,ifstream::in);
	  if (!readK.is_open()) {
		throw runtime_error(file + " that is a bad file.");}
	
	
	if(readK.peek() == std::ifstream::traits_type::eof()){
		 return false;
			}
			
	while(getline(readK,input)){
		input.erase(input.find_last_not_of(" \n\r\t\v\f")+1);
		int firstNotAlphabic = input.find_first_not_of(Alphabic);
		int firstspace = input.find_first_of(Space);
		
		if(firstNotAlphabic < firstspace){
			throw runtime_error( "Error: "+file + " contains bad contents : that is not alphanumeric");
			
			}
		if(firstspace >0){
			return false; //is not keyfile
			}
		}
	return true;//is keyfile
}



void Gallery::read(const string filename, const string keyfilename){
	ifstream readKey(keyfilename,ifstream::in);
	if(!readKey.is_open()){
		throw runtime_error(keyfilename+ " is a bad file.");}
	Enemy en(keyfilename);
		
		
	ifstream readFile(filename,ifstream::in);
		if(!readFile.is_open()){
		throw runtime_error(filename+ " is a bad file.");}
		
	bool readDone = en.read(readFile);
	while (readDone){
		//readDone  = en.read(readFile);
		add(en);
		readDone = en.read(readFile);
		}
	readFile.close();
	}


void Gallery::add(const Enemy& enemy){
	count++;
	Enemy en(enemy);
	en.setGallery(this);
	//KVpair.insert(pair<int,Enemy>(count,en));
	containers.push_back(en);
	}


void Gallery::clear(){
	containers.clear();
	}



size_t  Gallery::size() const{
	return containers.size();
	}


bool Gallery::empty() const{
	return containers.empty();
}


const Enemy* Gallery::get(size_t n) const{
	if(n>containers.size()){
		throw range_error( n + "this is erroneous and out of range.");
		}
	return  &containers[n]; 
	}
	
Enemy* Gallery::get(size_t n){
	if(n>containers.size()){
		throw range_error( n + "this is erroneous and out of range.");
		}
	return &containers[n];	
	}
	
const Enemy &Gallery::operator[](size_t n) const{
	if(n>=containers.size()){
		throw range_error( n + "this is out of range.");
		}
	return containers[n];
	}

Enemy &Gallery::operator[](size_t n){
	if(n>=containers.size()){
		throw range_error( n + "this is out of range.");
		}
	return containers[n];
			
	}
	
	
Gallery::operator bool()const{
	return !containers.empty();
	}
	
ostream &operator<<(std::ostream &stream,const Gallery &val){
	
	for(size_t i=0;i<val.size();i++){
			val.get(i)->write(stream);
			if(i== (val.size()-1)  ){
				
				}else{
					cout<<'\n';
					}
			
	}
	return stream;
}	

Gallery::iterator Gallery::begin() const{
	return iterator(containers,0);
	}
	
Gallery::iterator Gallery::end() const{
	return iterator(containers,size());
	}
	

ostream &operator<<(std::ostream &stream, Gallery &val){

	for(size_t i=0;i<val.size();i++){
			val.get(i)->write(stream);
			if(i== (val.size()-1)  ){
				
				}else{
					cout<<'\n';
					}
			
	}
	return stream;
}
