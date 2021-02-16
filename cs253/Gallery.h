#ifndef GALLERY_H_INCLUDE
#define GALLERY_H_INCLUDE


#include <cassert>
#include <cstddef>	
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
#include <algorithm>
#include <stdexcept>
#include "Enemy.h"

using std::string;
using std::cout;

class iterator{};

		
class Gallery{
	public:
		class iterator{
			public:	iterator(std::vector<Enemy> gallery,size_t i ) : containers(gallery),index(i){};
				/*iterator(const iterator &object) =default;
				~iterator();
				iterator &operator=(const iterator &object) =default;*/
				
				
				iterator &operator++(){
					//cout<<"this time is "<<index<<"\n";
					++index;
					return *this;
					};
				iterator operator++(int){
					//cout<<"this time is "<<index<<"\n";
					const auto save = *this;
					++index;
					return save;		
					};
				iterator &operator--(){
					//cout<<"minus is"<<index<<"\n";
					--index;
					return *this;
					};
				iterator operator--(int){
					//cout<<"minus is"<<index<<"\n";
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
				Enemy  operator*() const{
					//cout<<"return index is"<<index;
					return containers[index];
					};
				
				//mutable vector<Enemy> containers;
				//mutable int index;
			private:
				std::vector<Enemy> containers;
				size_t index;
			};
			
		iterator begin() const;
		iterator end() const;
		
		Gallery(const string&,const string&);
		Gallery(const string&,const string&,const string&);
		Gallery(const string&,const string&,const string&,const string&);
		Gallery(const string&,const string&,const string&,const string&,const string&);
		Gallery(const string&,const string&,const string&,const string&,const string&,const string&);
		Gallery(const Gallery&) ;	
		virtual ~Gallery();//Destructor
		Gallery &operator=(const Gallery&);
		
		
		
		void read(const string filename,const string keyfilename);
		void add(const Enemy& enemy);
		bool checkLegitKeyfile(string);
		void clear();
		size_t size() const;
		bool empty() const;
		const Enemy* get(size_t n) const;
		Enemy* get(size_t n);
		
		const Enemy &operator[](size_t index) const;
		Enemy &operator[](size_t index);
		operator bool()const;
		
		//iterator
		
		
	private: 
		int count = 0;
		 //std::map<int,Enemy> KVpair;
		 //std::pair<int,Enemy*> MyPair;
		 std::vector<Enemy> containers;
	};


/*class iterator{
			std::vector<Enemy> containers;
			size_t index;
			public:	iterator(std::vector<Enemy> gallery,size_t i ) : containers(gallery),index(i){};
				iterator(const iterator &object) =default;
				~iterator();
				iterator &operator=(const iterator &object) =default;
				
				
				iterator &operator++();
				iterator operator++(int);
				iterator &operator--();
				iterator operator--(int);
				bool operator==(const iterator &object) const;
				bool operator!=(const iterator &object) const;
				Enemy const* operator*() const;
				
				//mutable vector<Enemy> containers;
				//mutable int index;
			private:
		};*/

		
std::ostream &operator<<(std::ostream&,const Gallery&);
std::ostream &operator<<(std::ostream&,Gallery&);


#endif /*GALLERY_H_INCLUDE*/
