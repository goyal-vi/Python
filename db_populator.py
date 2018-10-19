import csv
import mysql.connector

db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="vishi@123",
        database="edulab"
        )
cursor = db.cursor()
with open("naukri_com/temp/naukri_dataanalytics.csv",mode = 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL, skipinitialspace=True)
    line_count = 0
    location = {}
    location_count = 0
    for row in csv_reader:
        if line_count == 0 or row["job_title"] == "":
            line_count += 1
            continue
        job_description = row["job_description"].replace('"','\\"')
        command01 = f'insert into dataanalyst_ncr(job_id, job_title, experience_required, company_name, link_to_job_description_page, keyskills, job_description, salary) values ({line_count - 1}, "{row["job_title"]}", "{row["experience_required"]}", "{row["company_name"]}", "{row["job_description_url"]}", "{row["key_skills"]}", "{job_description}", "{row["salary"]}");'
        #print(command01)
        cursor.execute(command01)
        db.commit()
        locations = row["location"]
        locations.replace('"', '')
        location_list = [x.strip() for x in locations.split(',')]
        location_list = set(location_list)
        for loc in location_list:
            if loc in location:
                location_id = location[loc]
            else:
                location_id = location_count
                location[loc] = location_id
                location_count += 1
            command02 = f'insert into location_jobs( job_id, locn_id, location) values ("{line_count-1 }", "{location_id}", "{loc}");'
            #print(command02)
            cursor.execute(command02)
            db.commit()
        line_count += 1
        
