#ifndef ENEMY_H_INCLUDE
#define ENEMY_H_INCLUDE



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


using std::string;
using std::map;
using std::pair;
class Gallery;





class Enemy{
	public:
	class iterator{
			
			
			public:	iterator(std::map<string,string> K,size_t i ) : KVpair(K),index(i){};
				/*iterator(const iterator &object) =default;
				~iterator();
				iterator &operator=(const iterator &object) =default;*/
				
				
				iterator &operator++(){
					++index;
					return *this;
					};
				iterator operator++(int){
					const auto save = *this;
					++index;
					return save;		
					};
				iterator &operator--(){
					--index;
					return *this;
					};
				iterator operator--(int){
					const auto save = *this;
					--index;
					return save;	
					};
				bool operator==(const iterator &object) const{
					return index == object.index;
					};
				bool operator!=(const iterator &object) const{
					return !(*this == object);
					};
				std::pair<string,string> operator*() const{
					map<string, string>::const_iterator itr; 
					size_t i=0;
					for(itr = KVpair.begin();itr !=KVpair.end();itr++){
	
								if(i == index){
											return pair<string,string>(itr->first,itr->second);}
											i++;
													}
					return pair<string,string>(itr->first,itr->second);
					};
			private:
				std::map<string,string> KVpair;
				size_t index;
		};
		iterator begin() const;
		iterator end() const;
		
		
		Enemy(string keyfile);
		Enemy(const Enemy&);	
		~Enemy();//Destructor
		 Enemy &operator=(const Enemy &);
		
		
		
		bool read(std::istream& in);
		void write(std::ostream& os) const;
		void write(string filename) const;
		string field(string key) const;
		bool compareKey();
		void show_name(bool n = true);
		void show_other(bool o = true);
		void show_link(bool l = true);
		//std::map<string,string> get_map() const;
		
		void clear();
		size_t size() const;
		bool empty() const;
		Enemy *link(string realtion) const;
		void setGallery(Gallery *gallery);
		
		std::string operator[](const string key) const;
		std::string operator[](const char* key) const;
		std::pair<string,string> operator[](size_t index) const;
		operator bool()const;
		bool operator==(const Enemy &)const;
		bool operator!=(const Enemy &)const;
		
	private: 
		int co=0;
		std::map<string,string> KVpair;
		bool n =true,o=true,l=true;
		std::vector<string> duplicateKeys;
		std::vector<string> checkKeys;
		Gallery* g;
	};



std::ostream &operator<<(std::ostream &,const Enemy&);
#endif /*ENEMY_H_INCLUDE*/
