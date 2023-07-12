# How to search for a CVE in metasploit
---

Use the following steps to search for a CVE manually, using `msfconsole`.


### Building & Running a metasploit container

To do this we will use the `debian-msf-local` docker container image.

A `Dockerfile` and build script (`build.sh`) has been included
to build a metasploit image from scratch.

Once the build script finishes, the container can be started using `run.sh`

---

Alternatively, if you have access to the attack-tools container registry:

Run the following command to run the Metasploit Base container.
```
docker run -i -t --network host --entrypoint /bin/bash us.gcr.io/attack-tools/rac-base-msf:1.3.16
```

This will start the container image for metasploit, based on the randori attack commons base image.

---

### Running Metasploit

Once running the metasploit container...

To run metasploit console, run the following command:

```
./msfconsole
```


To search for a specific CVE within the metasploit console, run the following command:
```
search cve:<CVE_ID_HERE>
```

For Example, searching for the recent moveit SQL injection CVE - CVE-2023-34362
```
search cve:CVE-2023-34362
```

You should see output like this:
```
msf6 > search cve:CVE-2023-34362

Matching Modules
================

   #  Name                                        Disclosure Date  Rank       Check  Description
   -  ----                                        ---------------  ----       -----  -----------
   0  exploit/windows/http/moveit_cve_2023_34362  2023-05-31       excellent  Yes    MOVEit SQL Injection vulnerability


Interact with a module by name or index. For example info 0, use 0 or use exploit/windows/http/moveit_cve_2023_34362
```


