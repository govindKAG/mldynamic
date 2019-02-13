import subprocess 
import shlex

#subprocess.run(["kubectl","logs","emote-trainb2-8xskr","-f"])
#subprocess.run(shlex.split('argo list'))
#subprocess.run(shlex.split('kubectl logs emote-trainb2-8xskr -f'))

def get_latest_argo_logs(train_job_name):
    argo_jobs = subprocess.check_output(shlex.split('argo list'))
    print(type(argo_jobs)) 
    argo_jobs = argo_jobs.decode('utf-8')
    print(type(argo_jobs))
    #print(argo_jobs)
    argo_jobs = argo_jobs.splitlines()
    #print(argo_jobs)
    
    latest_job = argo_jobs[1].split(' ')[0]
    print(latest_job)
    subprocess.run(shlex.split(f'argo logs -wf {latest_job}'))
    
    subprocess.run("kubectl logs  $(kubectl get pods | awk '/{job_name}/ {{print $1;exit}}')".format(job_name = train_job_name), shell=True)

get_latest_argo_logs('emote-trainb2')
