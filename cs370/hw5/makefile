JFLAGS = -g
JC = javac
.SUFFIXES: .java .class
.java.class:
	$(JC) $(JFLAGS) $*.java

CLASSES = \
	Buffer.java \
	Consumer.java \
	Producer.java \
	Coordinator.java 

default: classes

all: classes

classes: $(CLASSES:.java=.class)

clean:
	$(RM) *.class