#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <errno.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <sys/socket.h>
#include <string.h>
#include <netdb.h>
#include <netinet/in.h>

#include "gfclient.h"
#include "gfclient-student.h"

void gfc_cleanup(gfcrequest_t *gfr){

}

gfcrequest_t *gfc_create(){

    return (gfcrequest_t *)NULL;

}

size_t gfc_get_bytesreceived(gfcrequest_t *gfr){
    return -1;
}

size_t gfc_get_filelen(gfcrequest_t *gfr){
    return -1;
}

gfstatus_t gfc_get_status(gfcrequest_t *gfr){
    return -1;
}

void gfc_global_init(){
}

void gfc_global_cleanup(){
}

int gfc_perform(gfcrequest_t *gfr){
    return -1;
}

void gfc_set_headerarg(gfcrequest_t *gfr, void *headerarg){

}

void gfc_set_headerfunc(gfcrequest_t *gfr, void (*headerfunc)(void*, size_t, void *)){

}

void gfc_set_path(gfcrequest_t *gfr, char* path){

}

void gfc_set_port(gfcrequest_t *gfr, unsigned short port){

}

void gfc_set_server(gfcrequest_t *gfr, char* server){
  
}

void gfc_set_writearg(gfcrequest_t *gfr, void *writearg){

}

void gfc_set_writefunc(gfcrequest_t *gfr, void (*writefunc)(void*, size_t, void *)){
  
}

char* gfc_strstatus(gfstatus_t status){
    return (char *)NULL;
}

