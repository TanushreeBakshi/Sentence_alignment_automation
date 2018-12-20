//Pgm which takes its input from align.txt and displays the english and hindi aligned sentences in one text file
//./a.out align.txt hnd.txt eng.txt out.txt
#include<stdio.h>
#include<string.h>
#include<unistd.h>
#include<fcntl.h>
#include<stdlib.h>
int parse(char str[],int left[],int *leftsize,int right[],int *rightsize)
{
	int i=0;
	int j=0,k;
	for(k=0;k<10;k++)
	left[k]=right[k]=0;
	while(str[i]!='<')
	{
		if(str[i]==',')
			j++;
		else if(str[i]>='0'&&str[i]<='9')
			left[j]=left[j]*10+(str[i]-'0');
		else if(str[i]=='o')
		return -1;
	i++;
	}
	*leftsize=j;
	j=0;
	while(str[i]!='\n')
	{
		if(str[i]==',')
			j++;
		else if(str[i]>='0'&&str[i]<='9')
			right[j]=right[j]*10+(str[i]-'0');
		else if(str[i]=='o')
		return -2;
	i++;
	}
	*rightsize=j;
return 0;
}
					
int main(int argc,char *argv[])
{
	if(argc<5)
	printf("error");
	//system(strcpy("rm ",argv[4]));
	int fpa=open(argv[1],O_RDONLY,0777);//open align.txt in read only mode
	int fph=open(argv[2],O_RDONLY,0777);//open hnd.txt in read only mode
	int fpe=open(argv[3],O_RDONLY,0777);//open eng.txt in read only mode
	int fpo=open(argv[4],O_WRONLY|O_CREAT|O_TRUNC,0777);//open out.txt in write mode
	FILE *fa=fdopen(fpa,"r");
	FILE *fe=fdopen(fpe,"r");
	FILE *fh=fdopen(fph,"r");
	FILE *fo=fdopen(fpo,"w");
	char str[1000000], buf[1000000];
	int i,leftsize,rightsize,left[10],right[10], q, k;
	while(fgets(str,1000,fa)!=NULL)
	{
		char str1[100000];
		leftsize=0;rightsize=0;
		int status=parse(str,left,&leftsize,right,&rightsize);
		//fprintf(fo,"\n%d %d %d\n",status,leftsize,rightsize);
		if(status==-1){           //for cases like omitted <=> 1
		fgets(str1,100000,fh);
		
		continue;
		}
		if(status==-2)
		{                        //for cases like 1 <=> omitted
		fgets(str1,100000,fe);
	
		continue;
		}
		if(leftsize==rightsize)   //for cases like 1,2 <=> 1,2
		{
			i=0;	
			while(i!=(leftsize+1))
			{
				fgets(str1, 100000, fe);
				write(fpo, str1, strlen(str1)-1);
				write(fpo, " <=> ", 5);
				fgets(str1, 100000, fh);
				write(fpo, str1, strlen(str1)-1);
				write(fpo, "\n", 1);
				i++;
			}
		}
		else
		{
		i=0;                    //for cases like 1 <=> 2,3 or 1,2 <=> 3
		while(i!=leftsize)
		{
			fgets(str1, 100000, fe);
			k=0;
			for(q=0;str1[q]!='\0'; q++)
			{
				if((str1[q]=='.' || str1[q]=='!' || str1[q]=='?') && str1[q+1]=='\n')
					break;
				else if((str1[q]=='"' || str1[q]==')') && str1[q+1]=='\n')
				{
					buf[k++]=str1[q];
					break;					
				}
				else 
					buf[k++]=str1[q];
			}
			i++;
			write(fpo, buf, k);
			write(fpo, " ; ", 3);

		}
		
		fgets(str1, 100000, fe);
		write(fpo, str1, strlen(str1)-1);

		
		write(fpo," <=> ",5);
				
		/*for(i=0;;i++)
		{

		fgets(str1,100000,fh);
		write(fpo,str1,strlen(str1)-2);

		if(i==rightsize)
		{
			write(fpo, ".",1);
			break;
			
		}
		write(fpo," ; ",3);

		}*/
		i=0;
		while(i!=rightsize)
		{
			fgets(str1, 100000, fh);
			k=0;
			for(q=0;str1[q]!='\0'; q++)
			{
				if(str1[q]=='.' && str1[q+1]=='\n')
					break;
				else if((str1[q]=='"' || str1[q]==')') && str1[q+1]=='\n')
				{
					buf[k++]=str1[q];
					break;					
				}
				else 
					buf[k++]=str1[q];
			}
			i++;
			write(fpo, buf, k);
			write(fpo, " ; ", 3);

		}
		fgets(str1, 100000, fh);
		write(fpo, str1, strlen(str1)-1);


		write(fpo,"\n",1);
	//close(fpo);close(fpe);close(fph);close(fpa);
	}
	}
return 0;
}
