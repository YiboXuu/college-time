#include "Enemy.h"
#include "Gallery.h"
#include <iostream>
#include <istream>
#include <vector>
#include <numeric>
#include <algorithm>
#include <ctype.h>
#include <fstream>
#include <map>
#include <string>
#include <cctype>
#include <iterator>
#include <sstream>
using namespace std;

Enemy::Enemy(const Enemy &rhs){
	co= rhs.co;
	 KVpair = rhs.KVpair;
	 g = rhs.g;
	n =rhs.n;
	o = rhs.o;
	l=rhs.l;
	checkKeys = rhs.checkKeys;
	duplicateKeys = rhs.duplicateKeys;
	}
	
Enemy::~Enemy(){
	}
	

Enemy &Enemy::operator=(const Enemy &rhs) {
    co = rhs.co;
    KVpair = rhs.KVpair;
    g = rhs.g;
    n =rhs.n;
	o = rhs.o;
	l=rhs.l;
	checkKeys = rhs.checkKeys;
	duplicateKeys = rhs.duplicateKeys;
    return *this;
}

Enemy::Enemy(string keyfile){
	string Alphabic = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890";
	ifstream in(keyfile,ifstream::in);
	if (!in.is_open()) {
		exit(1);}
		string key;
	while(getline(in,key)){
		
		int length = key.find_first_not_of(Alphabic);
		if(length  <    static_cast<int> (key.length()) && length!=-1){
			//cout<<length<<'\n';
					throw runtime_error(keyfile+ " :this is not alphanumeric " +key);
		}
		checkKeys.push_back(key);
	}
		
}
	
bool Enemy::read(istream& in){
	if(!KVpair.empty()){
		KVpair.clear();
	}
	string Alphabic = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890";
	string Space = " \t\n\f\v"; 
int	firstNotSpace ;
int firstNotAlphabic;
string key;
string input;
//cout<<11111<<'\n';
bool isStart = true;
string addToValues;


while(getline(in,input)){
	//cout<<"current size:"<<this->KVpair.size()<<'\n';
	//cout<<input;
	input.erase(input.find_last_not_of(" \n\r\t\v\f")+1);
	//cout<<input<<'\n';
	char c = in.peek();
	if(isStart == true && isspace(c)) {
		//getline(in, input);
		//continue;
	}
	//cout << "Is it a start of the Enemey? " << isStart << "\n";
	if(!input.length() == 0){
		co++;
		firstNotSpace = input.find_first_not_of(Space);
		firstNotAlphabic =input.find_first_of(Space);
		
		
		if(firstNotSpace>0){
					int lastAlphabic = input.find_last_of(Alphabic);
					
					int z = lastAlphabic -firstNotSpace+1;
					addToValues.assign(input,firstNotSpace,z);
					
					map<string,string>::iterator itr = this-> KVpair.find(key);
					if(itr != this->KVpair.end()) {
						itr -> second = itr -> second.append(" "+addToValues);
					}
				   isStart=false;
		}else{	 
				key.assign(input,0,firstNotAlphabic);//assign key
				if(!count(checkKeys.begin(),checkKeys.end(),key)){
							throw runtime_error("this is not in keyfile: "  +  key);
				}
					
				for(size_t j=0;j<key.length();j++){
					if(!isalnum(key.at(j))){
						throw runtime_error("this is not alphanumeric " + key);	
						}
					}
					//cout << "Current Key is: " << key << "\n";
					input.erase(0,firstNotAlphabic); //remove key;
					if(input.empty()) {
							getline(in, input);
							firstNotSpace = input.find_first_not_of(Space); //remove space;
							input.erase(0,firstNotSpace);
							//cout<<input<<"\n";
							map<string,string>::iterator itr = this-> KVpair.find(key) ;
							//cout<<key<<"\n";
							if(itr != this->KVpair.end()) {
						//cout<<addToValues;
								itr -> second = itr -> second.append(" "+addToValues);
											}
						}
					firstNotSpace = input.find_first_not_of(Space); //remove space;
					input.erase(0,firstNotSpace);
					
					//cout << "Current Key is: " << key << "\n";
					for(size_t k=0;k<duplicateKeys.size();k++){
								string kkk = duplicateKeys[k];
							if(key == kkk){
								throw runtime_error("this is duplicate keys: " + key);
								}
							}
					duplicateKeys.push_back(key);
					KVpair.insert(pair<string,string>(key,input));
					//cout << "Current map size: " << this->KVpair.size() << "\n";
					
					isStart =false;
				}
				}	
						
		else{
				
				if(this -> KVpair.size() != 0) {
					//cout<<this->KVpair.size()<<"\n";
					if(!count(duplicateKeys.begin(),duplicateKeys.end(),"Name")){
												throw runtime_error("No name key");
											}
								duplicateKeys.clear();
								return true;
				}
					
					this->clear();
				//duplicateKeys.clear();
				co=0;
		}		
		
	}
	
	if(this -> KVpair.size() != 0) {
					//cout<<this->KVpair.size()<<"\n";
					//cout<<this->KVpair.size()<<"\n";
					if(!count(duplicateKeys.begin(),duplicateKeys.end(),"Name")){
												throw runtime_error("No name key");
											}
										duplicateKeys.clear();
								return true;
				}
		this->clear();
		//duplicateKeys.clear();
		//cout << "Map size after reading enemy:  " << this -> KVpair.size() << "\n";
		return false;
}


		
void Enemy::write(ostream &os) const{
	int oLength =0;
	int lLength =0;
	int lkeyLength =0;
	int okeyLength =0;
	int nkeyLength =4;
	int max=0;
	int spaceCounter;
	map<string, string>::const_iterator itr; 
	bool foundLink;
	bool foundName;
for(itr = KVpair.begin();itr !=KVpair.end();itr++){
		 foundLink = itr->first.find("Link")==0;
	if(foundLink){
		lLength = itr->first.length();
		//os<<  itr->first;
		if(lLength>lkeyLength){
			lkeyLength = lLength;}	
		}
	}

//cout<<lkeyLength<<'\n';

for(itr = KVpair.begin();itr !=KVpair.end();itr++){
		foundLink = itr->first.find("Link") ==0;
		foundName = itr->first.find("Name") ==0;
	if(!foundLink && !foundName){
		oLength = itr->first.length();
		//os<< itr->first;
		if(oLength>okeyLength){
			okeyLength = oLength;}	
		}
	}
//cout<<okeyLength<<'\n';
		
if(n==true&&l==true&&o==true){
	if(okeyLength>lkeyLength && okeyLength > nkeyLength){
		max = okeyLength;}
	else if(nkeyLength > okeyLength && nkeyLength > lkeyLength){
		max = nkeyLength;}
	else{
		max = lkeyLength;}
		//cout<<max;
	
	
	
	for(itr = KVpair.begin();itr !=KVpair.end();itr++){
		spaceCounter = max - itr->first.length() + 1;
		foundLink = itr->first.find("Link") ==0;
		foundName = itr->first.find("Name")==0;
		if(foundName){
			
					os<<  itr->first;
				for(int i=0;i<spaceCounter;i++)
					os<<" ";
				os<< itr->second<<'\n';		
					}
					
	}

	for(itr = KVpair.begin();itr !=KVpair.end();itr++){
		spaceCounter = max - itr->first.length() + 1;
		foundLink = itr->first.find("Link")==0;
		foundName = itr->first.find("Name")==0;
		if(!foundName && !foundLink){
					os<<  itr->first;
				for(int i=0;i<spaceCounter;i++)
					os<<" ";
				os<< itr->second<<'\n';		
					}
					
	}
	

	for(itr = KVpair.begin();itr !=KVpair.end();itr++){
		spaceCounter = max - itr->first.length() + 1;
		 foundLink = itr->first.find("Link") == 0;
		 foundName = itr->first.find("Name") == 0;
		 bool foundHttp =itr->second.find("http") ==0;
			if(foundLink && !foundHttp){
					os<<  itr->first;
				for(int i=0;i<spaceCounter;i++)
					os<<" ";
				os<< itr->second<<'\n';		
					}
	}
	
	for(itr = KVpair.begin();itr !=KVpair.end();itr++){
		spaceCounter = max - itr->first.length() + 1;
		 foundLink = itr->first.find("Link") == 0;
		 foundName = itr->first.find("Name") == 0;
		 bool foundHttp =itr->second.find("http") ==0;
			if(foundLink && foundHttp){
					os<<  itr->first;
				for(int i=0;i<spaceCounter;i++)
					os<<" ";
				os<< itr->second<<'\n';		
					}
	}
	
	
}
else if(n==true&&l==true){
	 if(nkeyLength > lkeyLength){
		max = nkeyLength;}
	else{
		max = lkeyLength;}
	
	
	
	for(itr = KVpair.begin();itr !=KVpair.end();itr++){
		spaceCounter = max - itr->first.length() + 1;
		foundLink = itr->first.find("Link") ==0;
		foundName = itr->first.find("Name")==0;
		if(foundName){
			
					os<<  itr->first;
				for(int i=0;i<spaceCounter;i++)
					os<<" ";
				os<< itr->second<<'\n';		
					}
					
	}

	for(itr = KVpair.begin();itr !=KVpair.end();itr++){
		spaceCounter = max - itr->first.length() + 1;
		 foundLink = itr->first.find("Link") == 0;
		 foundName = itr->first.find("Name") == 0;
		 bool foundHttp =itr->second.find("http") ==0;
			if(foundLink && !foundHttp){
					os<<  itr->first;
				for(int i=0;i<spaceCounter;i++)
					os<<" ";
				os<< itr->second<<'\n';		
					}
	}
	
	for(itr = KVpair.begin();itr !=KVpair.end();itr++){
		spaceCounter = max - itr->first.length() + 1;
		 foundLink = itr->first.find("Link") == 0;
		 foundName = itr->first.find("Name") == 0;
		 bool foundHttp =itr->second.find("http") ==0;
			if(foundLink && foundHttp){
					os<<  itr->first;
				for(int i=0;i<spaceCounter;i++)
					os<<" ";
				os<< itr->second<<'\n';		
					}
	}
	
}
else if(n==true&&o==true){
	 if(nkeyLength > okeyLength){
		max = nkeyLength;}
	else{
		max = okeyLength;}
	
	for(itr = KVpair.begin();itr !=KVpair.end();itr++){
		spaceCounter = max - itr->first.length() + 1;
		foundLink = itr->first.find("Link") ==0;
		foundName = itr->first.find("Name")==0;
		if(foundName){
			
					os<<  itr->first;
				for(int i=0;i<spaceCounter;i++)
					os<<" ";
				os<< itr->second<<'\n';		
					}
					
	}

	for(itr = KVpair.begin();itr !=KVpair.end();itr++){
		spaceCounter = max - itr->first.length() + 1;
		foundLink = itr->first.find("Link")==0;
		foundName = itr->first.find("Name")==0;
		if(!foundName && !foundLink){
					os<<  itr->first;
				for(int i=0;i<spaceCounter;i++)
					os<<" ";
				os<< itr->second<<'\n';		
					}
					
	}
}
else if(l==true&&o==true){
	if(okeyLength>lkeyLength){
		max = okeyLength;
	}else{
		max = lkeyLength;}

	for(itr = KVpair.begin();itr !=KVpair.end();itr++){
		spaceCounter = max - itr->first.length() + 1;
		foundLink = itr->first.find("Link")==0;
		foundName = itr->first.find("Name")==0;
		if(!foundName && !foundLink){
					os<<  itr->first;
				for(int i=0;i<spaceCounter;i++)
					os<<" ";
				os<< itr->second<<'\n';		
					}
					
	}
	

	for(itr = KVpair.begin();itr !=KVpair.end();itr++){
		spaceCounter = max - itr->first.length() + 1;
		 foundLink = itr->first.find("Link") == 0;
		 foundName = itr->first.find("Name") == 0;
		 bool foundHttp =itr->second.find("http") ==0;
			if(foundLink && !foundHttp){
					os<<  itr->first;
				for(int i=0;i<spaceCounter;i++)
					os<<" ";
				os<< itr->second<<'\n';		
					}
	}
	
	for(itr = KVpair.begin();itr !=KVpair.end();itr++){
		spaceCounter = max - itr->first.length() + 1;
		 foundLink = itr->first.find("Link") == 0;
		 foundName = itr->first.find("Name") == 0;
		 bool foundHttp =itr->second.find("http") ==0;
			if(foundLink && foundHttp){
					os<<  itr->first;
				for(int i=0;i<spaceCounter;i++)
					os<<" ";
				os<< itr->second<<'\n';		
					}
	}
	
	
}
else if(n==true){
	max = 4;
	
	
	for(itr = KVpair.begin();itr !=KVpair.end();itr++){
		spaceCounter = max - itr->first.length() + 1;
		//foundLink = itr->first.find("Link") ==0;
		foundName = itr->first.find("Name")==0;
		if(foundName){
			
					os<<  itr->first;
				for(int i=0;i<spaceCounter;i++)
					os<<" ";
				os<< itr->second<<'\n';		
					}
					
	}
}
else if(o==true){
	max = okeyLength;

	for(itr = KVpair.begin();itr !=KVpair.end();itr++){
		spaceCounter = max - itr->first.length() + 1;
		foundLink = itr->first.find("Link")==0;
		foundName = itr->first.find("Name")==0;
		if(!foundName && !foundLink){
					os<<  itr->first;
				for(int i=0;i<spaceCounter;i++)
					os<<" ";
				os<< itr->second<<'\n';		
					}
					
	}
}else if(l==true){
	max = lkeyLength;
	
	for(itr = KVpair.begin();itr !=KVpair.end();itr++){
		spaceCounter = max - itr->first.length() + 1;
		 foundLink = itr->first.find("Link") == 0;
		 foundName = itr->first.find("Name") == 0;
		 bool foundHttp =itr->second.find("http") ==0;
			if(foundLink && !foundHttp){
					os<<  itr->first;
				for(int i=0;i<spaceCounter;i++)
					os<<" ";
				os<< itr->second<<'\n';		
					}
	}
	
	for(itr = KVpair.begin();itr !=KVpair.end();itr++){
		spaceCounter = max - itr->first.length() + 1;
		 foundLink = itr->first.find("Link") == 0;
		 foundName = itr->first.find("Name") == 0;
		 bool foundHttp =itr->second.find("http") ==0;
			if(foundLink && foundHttp){
					os<<  itr->first;
				for(int i=0;i<spaceCounter;i++)
					os<<" ";
				os<< itr->second<<'\n';		
					}
	}

}
	
}
	
	
	
void Enemy::write(string filename) const{
	ofstream os;
	os.open(filename);
	
	if(!os){
		throw runtime_error("the file: " +filename +" can't be open");
		}
	int oLength =0;
	int lLength =0;
	int lkeyLength =0;
	int okeyLength =0;
	int max=0;
	int spaceCounter;
	map<string, string>::const_iterator itr; 
	bool foundLink;
	bool foundName;
for(itr = KVpair.begin();itr !=KVpair.end();itr++){
		 foundLink = itr->first.find("Link")==0;
	if(foundLink){
		lLength = itr->first.length();
		//os<<  itr->first;
		if(lLength>lkeyLength){
			lkeyLength = lLength;}	
		}
	}

//cout<<lkeyLength<<'\n';

for(itr = KVpair.begin();itr !=KVpair.end();itr++){
		foundLink = itr->first.find("Link") ==0;
		foundName = itr->first.find("Name") ==0;
	if(!foundLink && !foundName){
		oLength = itr->first.length();
		//os<< itr->first;
		if(oLength>okeyLength){
			okeyLength = oLength;}	
		}
	}
//cout<<okeyLength<<'\n';
		
if(n==true&&l==true&&o==true){
	if(okeyLength>lkeyLength){
		max = okeyLength;
	}else{
		max = lkeyLength;}
		//cout<<max;
	
	
	
	for(itr = KVpair.begin();itr !=KVpair.end();itr++){
		spaceCounter = max - itr->first.length() + 1;
		foundLink = itr->first.find("Link") ==0;
		foundName = itr->first.find("Name")==0;
		if(foundName){
			
					os<<  itr->first;
				for(int i=0;i<spaceCounter;i++)
					os<<" ";
				os<< itr->second<<'\n';		
					}
					
	}

	for(itr = KVpair.begin();itr !=KVpair.end();itr++){
		spaceCounter = max - itr->first.length() + 1;
		foundLink = itr->first.find("Link")==0;
		foundName = itr->first.find("Name")==0;
		if(!foundName && !foundLink){
					os<<  itr->first;
				for(int i=0;i<spaceCounter;i++)
					os<<" ";
				os<< itr->second<<'\n';		
					}
					
	}
	

	for(itr = KVpair.begin();itr !=KVpair.end();itr++){
		spaceCounter = max - itr->first.length() + 1;
		 foundLink = itr->first.find("Link") == 0;
		 foundName = itr->first.find("Name") == 0;
		 bool foundHttp =itr->second.find("http") ==0;
			if(foundLink && !foundHttp){
					os<<  itr->first;
				for(int i=0;i<spaceCounter;i++)
					os<<" ";
				os<< itr->second<<'\n';		
					}
	}
	
	for(itr = KVpair.begin();itr !=KVpair.end();itr++){
		spaceCounter = max - itr->first.length() + 1;
		 foundLink = itr->first.find("Link") == 0;
		 foundName = itr->first.find("Name") == 0;
		 bool foundHttp =itr->second.find("http") ==0;
			if(foundLink && foundHttp){
					os<<  itr->first;
				for(int i=0;i<spaceCounter;i++)
					os<<" ";
				os<< itr->second<<'\n';		
					}
	}
	
	
}
else if(n==true&&l==true){
		max = lkeyLength;
		//cout<<max;
	
	
	
	for(itr = KVpair.begin();itr !=KVpair.end();itr++){
		spaceCounter = max - itr->first.length() + 1;
		foundLink = itr->first.find("Link") ==0;
		foundName = itr->first.find("Name")==0;
		if(foundName){
			
					os<<  itr->first;
				for(int i=0;i<spaceCounter;i++)
					os<<" ";
				os<< itr->second<<'\n';		
					}
					
	}

	for(itr = KVpair.begin();itr !=KVpair.end();itr++){
		spaceCounter = max - itr->first.length() + 1;
		 foundLink = itr->first.find("Link") == 0;
		 foundName = itr->first.find("Name") == 0;
			if(foundLink){
					os<<  itr->first;
				for(int i=0;i<spaceCounter;i++)
					os<<" ";
				os<< itr->second<<'\n';		
					}
	}
	
}
else if(n==true&&o==true){
	max = okeyLength;
	
	
	for(itr = KVpair.begin();itr !=KVpair.end();itr++){
		spaceCounter = max - itr->first.length() + 1;
		foundLink = itr->first.find("Link") ==0;
		foundName = itr->first.find("Name")==0;
		if(foundName){
			
					os<<  itr->first;
				for(int i=0;i<spaceCounter;i++)
					os<<" ";
				os<< itr->second<<'\n';		
					}
					
	}

	for(itr = KVpair.begin();itr !=KVpair.end();itr++){
		spaceCounter = max - itr->first.length() + 1;
		foundLink = itr->first.find("Link")==0;
		foundName = itr->first.find("Name")==0;
		if(!foundName && !foundLink){
					os<<  itr->first;
				for(int i=0;i<spaceCounter;i++)
					os<<" ";
				os<< itr->second<<'\n';		
					}
					
	}
}
else if(l==true&&o==true){
	if(okeyLength>lkeyLength){
		max = okeyLength;
	}else{
		max = lkeyLength;}

	for(itr = KVpair.begin();itr !=KVpair.end();itr++){
		spaceCounter = max - itr->first.length() + 1;
		foundLink = itr->first.find("Link")==0;
		foundName = itr->first.find("Name")==0;
		if(!foundName && !foundLink){
					os<<  itr->first;
				for(int i=0;i<spaceCounter;i++)
					os<<" ";
				os<< itr->second<<'\n';		
					}
					
	}
	

	for(itr = KVpair.begin();itr !=KVpair.end();itr++){
		spaceCounter = max - itr->first.length() + 1;
		 foundLink = itr->first.find("Link") == 0;
		 foundName = itr->first.find("Name") == 0;
			if(foundLink){
					os<<  itr->first;
				for(int i=0;i<spaceCounter;i++)
					os<<" ";
				os<< itr->second<<'\n';		
					}
	}
	
	
}
else if(n==true){
	max = 4;
	
	
	for(itr = KVpair.begin();itr !=KVpair.end();itr++){
		spaceCounter = max - itr->first.length() + 1;
		//foundLink = itr->first.find("Link") ==0;
		foundName = itr->first.find("Name")==0;
		if(foundName){
			
					os<<  itr->first;
				for(int i=0;i<spaceCounter;i++)
					os<<" ";
				os<< itr->second<<'\n';		
					}
					
	}
}
else if(o==true){
	max = okeyLength;

	for(itr = KVpair.begin();itr !=KVpair.end();itr++){
		spaceCounter = max - itr->first.length() + 1;
		foundLink = itr->first.find("Link")==0;
		foundName = itr->first.find("Name")==0;
		if(!foundName && !foundLink){
					os<<  itr->first;
				for(int i=0;i<spaceCounter;i++)
					os<<" ";
				os<< itr->second<<'\n';		
					}
					
	}
}else if(l==true){
	max = lkeyLength;
	
	for(itr = KVpair.begin();itr !=KVpair.end();itr++){
		spaceCounter = max - itr->first.length() + 1;
		 foundLink = itr->first.find("Link") == 0;
		 foundName = itr->first.find("Name") == 0;
			if(foundLink){
					os<<  itr->first;
				for(int i=0;i<spaceCounter;i++)
					os<<" ";
				os<< itr->second<<'\n';		
					}
	
	}

}
		
	
	os.close();
	}



string Enemy::field(string key) const{
	if(this->KVpair.find(key) ==KVpair.end()){
			throw range_error("ERROR from field : This is bad key: " + key);
		}
	return this->KVpair.at(key);
		
	
	}
	
void Enemy::show_name(bool name){
	if(name == false){
			n =false;
		}else{
			n =true;
			}
	
	}
	
void Enemy::show_other(bool other){
	if(other ==false){	
			o=false;
		}else{
			o=true;
		}
	}

void Enemy::show_link(bool link){
	if(link ==false){	
			l=false;
		}else{
			l=true;}
	}
	
	
void Enemy::clear(){
	KVpair.clear();
	}



size_t  Enemy::size() const{
	return this->KVpair.size();
	}


bool Enemy::empty() const{
	return (this->KVpair.size() == 0);
}

void Enemy::setGallery(Gallery* newone){
	g =newone;
	}
Enemy* Enemy::link(string relation) const{
	string key = "Link"+relation;
	string value = this->field(key);
	for(size_t i=0;i<g->size();i++){
		Enemy* enemy = g->get(i);
		
	
		string enemyValue = enemy->field("Name");
	if(value == enemyValue){
			return enemy;
			}
		}
	throw range_error("didn't find link" +relation + "in this gallery");

	}
string Enemy::operator[](const char* key) const{
	//field help me to check there is a range_error 
			string s(key);
			return field(s);
	}
	
string Enemy::operator[](const string key) const{
	//field help me to check there is a range_error 
			return field(key);
	}
pair<string,string> Enemy::operator[](size_t index) const{
	map<string, string>::const_iterator itr; 
	size_t i=0;
	if(this->KVpair.size() == 0 ){
		throw range_error("this index is out of range: "  +index);
		}
	
	if(index>= KVpair.size() ){
		throw range_error("this index is out of range: "  +index);
		}
	
	for(itr = KVpair.begin();itr !=KVpair.end();itr++){
	
		if(i == index){
				return pair<string,string>(itr->first,itr->second);}
			i++;
	}
		return pair<string,string>(itr->first,itr->second);
	}

Enemy::operator bool()const{
	return !KVpair.empty();
	}


bool Enemy::operator==(const Enemy &a)const{
		map<string, string>::const_iterator itr;
	if(size() !=a.size()){
		return false;
	}else{
	
	for(itr = KVpair.begin();itr !=KVpair.end();itr++){
			try{
				if(field(itr->first) != a.field(itr->first)){
				return false;}
			}catch(range_error &err){
				//if(itr->first != )
				return false;
				}
			
			}
		}
			return true;
	}


bool Enemy::operator!=(const Enemy &a)const{
	return !(a==*this);
	}

Enemy::iterator Enemy::begin() const{
	return iterator(KVpair,0);
	}

Enemy::iterator Enemy::end() const{
	return iterator(KVpair,size());
	}
	
ostream &operator<<(ostream &stream,const Enemy &val) {
	val.write(stream);
	return stream;
}
