create database edulab;
use edulab;
create table dataanalyst_ncr(
	job_title varchar(255),
	experience_required varchar(255),
	company_name varchar(255),
	link_to_job_description_page text,
	keyskills varchar(255),
	job_description varchar(255),
	salary varchar(255),
	job_id int,
	last_updated_on datetime default current_timestamp on update current_timestamp,
	primary key(job_id));


create table location_jobs(
	job_id int,
	locn_id int,
	location varchar(255),
	primary key(job_id, location_id),
	foreign key(job_id) references dataanalyst_ncr(job_id));
