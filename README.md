# Logs Analysis Project

This project is about building an internal reporting tool that will use information from the database to discover what kind of articles the site's readers like.
Program run from the command line. It won't take any input from the user. Instead, it will connect to that database, use SQL queries to analyze the log data, and print out the answers to 3 questions:
1. What are the most popular three articles of all time? 
2. Who are the most popular article authors of all time? 
3. On which days did more than 1% of requests lead to errors?

# Installing
To start on this project, you'll need database software (provided by a Linux virtual machine) and the data to analyze.

### The virtual machine
To install virtualBox on your computer please check the following [link](https://classroom.udacity.com/nanodegrees/nd004/parts/8d3e23e1-9ab6-47eb-b4f3-d5dc7ef27bf0/modules/bc51d967-cb21-46f4-90ea-caf73439dc59/lessons/5475ecd6-cfdb-4418-85a2-f2583074c08d/concepts/14c72fe3-e3fe-4959-9c4b-467cf5b7c3a0) (step by step installation) or download it directly from [VirtualBox](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1) and [Vagrant](https://www.vagrantup.com/downloads.html)
 
 
 ### Download the VM configuration
You can download [a zip file](https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip) or you can use Github to fork and clone the [repository](https://github.com/udacity/fullstack-nanodegree-vm.)

### Start the virtual machine
Inside your directory containing the VM files

![](https://lh3.googleusercontent.com/B8zrxWe1BgLVa-wK-I4B4RKsPgg6i7q26LDfy9uMt_o361I4XHUV3Gf5ATsmp_fyq_c9EId4owvjY1-q-ynPVYKIcNk6BVHaLITuENEtruwLWkSl6baDm4LfOkOrs7k1dJ2P8qb4IulAUAM4D90T1cQ1wLhHxO-kc9gP_T9Q43OiuVFo-bfy8c_jlq_0kPYeHPhRpiuBP5LfheyrJnRC5LNZ5h5lQpH3PmO0RZBuE9j4G2LTRbBVc76E1gi4PQMHJD6ldDOSrNrV6BICY0quakpIxQUckCmm8sVY_usm9cSyaNiVdUfdEdKhv_BqbCS4gcJoifHNiqxLEJYj4eKjXsrLA2P9eknihpUgR46SNqkJ9iyrBuby8CaTc4iNO7r08Mm5H2xP5P6zITzffxBiXH8StopfGmXq1oNimQo7ovgpPuYlA-7jv0z0EARTwl1iYMxfxdvPvsNfAepcUn0BEzpW1jRjzqqt8XPp3ia9PiGa4LCgbWz1Ngc9ne_XtVxI1okOxECbBB69znqTPbe7ugRd2M2c9mwZvjZhVvt4RRKaWL_vx7NGy33ioClzgxfB-BRzZ5Q7HzbM2tgE9cpc-rVzdQbs3Xzuo-ni9eQ=w540-h123-no) 

go to vagrant subdirectory and run the command `vagrant up`.

![](https://lh3.googleusercontent.com/cyePVmsMEd8rIGCqSVAJGsdA6cUhiiIhKJ4J7bNNRTnS841MtdAM94HGmtZC6kiJ1AfA5hIsTHYvUzcrzJuEA-tOFnQBA-X4ZcyJ-wUkO-mapzOvLph7wlWIRyi_rXsBYxt2JFxL5IP_U22cxDOQacibHP4AOnHOZ9ACzwhTSgyNxH4mWw91x-S8hCY7t_1YyQLAJs0QPnqnKfI7JMdBuo2CSyXd7ZHz22BWJQl7UR8gT-puu9Svx_MIqhjnTOQwDhcysB8ygLtJYpEJJapivqDiOYWD7XeIpmRAqHKDWPt6j0HdHi6DaoJY1cUzOk_zniDfXiVm_kEbfq252M-wsyWtUpeCYyz0lGBFzVr40dOlu3JuhD6tHmxKvEzSNNPF40vViU-pb6s-AJjLluBR_8Y-Ylx1vkAG_QXk-Vz5IXyyrXsQdvPVIQkQcmFryrBGkVK5_xkl3nuNn8SFLMNKtQdNPCp8pvhJayil0rcG5P1elRCHpWiq6LN6Lxvtv2YcmjvYdynmOi32f7diZ10aPP9Ch-KvjmPBS1ksRpTiHHWvu3UoYssSHWRbxanH0P-BG8HzIMuCPU8mpWP8nGTgMfOfg8eZfGDePP_JtAU=w465-h84-no)

When vagrant up is finished running, you will get your shell prompt back. Run `vagrant ssh` to log in to your newly installed Linux VM!

![](https://lh3.googleusercontent.com/vcMK0rJb_uqhMgvtqvPDrwBg_VQmN0BcnqIAEYFbn_Np5ZtZCgA8QtTpkmgM9JZt62mM8sPHyLPKTJUsUIKV58wtrx3yL1PiYbPs0ov_Fh8VBJOzlfvs9Po6cxwsAcwVdBssH8LqhrYBDPKlW6Zyi0qctyrPUaTw1I6gGtxGeIGsQikux9utAlseYCyIs0u47fIFZpB6oiE84-G8PCuzko0Lnp8IH3D1nSnyN_kywmcRonyyO_gd4FPTm0ElQekAAEqqKhR8MrXUlZMLENCd6r9R3uNkrqiewj2hCIjACZ0X6kc9eoY-aV6jyVEX2nf4LHBzNqu6-SBjM8R6anY-2ICjwimLs3UcOc1HlyluyYEsifgvEH9nbwyhS2u2lOqod3Jv8R_fhvp_xARlItUh0sy0QuuXNqAlSaRa8m7L64phvaDyNzIfBj_0AkeAbLEwSkU6g4HFwWTB32jwansrPQzwesriUQfbvyUybIc6HRj4csIGl58p6UaWbUo4xolvzkTaavVgD987v9nAFwD9F-hXaPDxqdJU6cd5_HR_2zKsMdIPaIHZNZK91ERFDNTG3iAJA9EVJuz2_7PAgLOLguaTMzQjW_1abnYlOBk=w532-h449-no)


### Download the data
[Download data from here ](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip"). Downloaded file is called `newsdata.sql` that you need to put it into the vagrant directory, which is shared with your virtual machine.
Now connect to your installed database server with `psql -d news -f newsdata.sql` command

![](https://lh3.googleusercontent.com/XPwZ0fOefvRRFlthTCs9NsRZ7jE2kZEQ-U6fcoUHCk0-pWwB1PZKs2p6DES0JIBxC1uenu039qjpOODgOSVtngHiRb24HR4uGpoQvR8VoOjsGxD8ZvBACQz1XLcJFMRovooLpV-N7AG42iNyLKJN5cZzG_8oCrUTFV8vCly2mz-gfoUqG6_QHli-CBMnaxs7Y_QkGPUp_Min0CaI8FDnMLyny5rlVRqSSFB8CtWkGPhdCw9Qev-x219fDyPomqAJPErfDvTvwSwgXkEMJhGkdz7JgdBVSOOJmacvex5z4BDAIFrxQKAsPO_wOxMnh4rltwEm_70bEXU_jncuFUwPQ3RRZHWwYQ17WxmkdxBKQFR2NSoSuStnwA_VgvWeEXFAjuR-BqHQmeo3v2B7cmKax2r5KSKnj5ccAYiZylclbjUfjFKcqPRC9oLlQYnsmIMsayxsk3wC2Wi_Z-wKE5CFpvcx4HmbuYfDczYbCbBJZC8FSzlAb0iR4IZI5DGScMTYlZ_YzWrSqWZ7G6vM9mYTPKwuSR6Jobc6BAKw3ltjUxfjDicE3eTTAU6Iz-C7doui4jYEd-4fqJR7FFeUfFYlh8FLGaDAqDGD3ocM8IY=w387-h69-no)

### Inside news database
To connect to database use `psql -d news` 

![](https://lh3.googleusercontent.com/fTJR1x6jmcpFjPYDfUKcH7eoqtONruI3S0odB9bmycVqNIId9bD_yEbeKFzWoOoTJpMZAbxwdkH6_8bXr9AOmnEajWqY3ZLtH9gpy1PAk4UlJNC0t6hF1rT0R-jUvEySMCVpngbeGy4wAWCZrLLmyLALmn5coRkC7q_BJRtiZ_VHYLCqIRpyboeSW39Kl62VfffKqia4oOhH2Ucbm0n1IdB4875Fg0gIv9Xxf0FN9NeIV0g_x6yvh1lE9ClT8fS8ikZXixl8p7sK7ze0-55jMncXmVPTeywFORQ3OJ3NJ7pOPIcbCVJiGPJ_rmW0qVsGisjUIOk_gYWMiIX_ddkpYJwIT2x4Q4-_G7kSmDG33NVyywiL8LPK2qLq2PlNTnKZrI0T5rb8DSad77M8Fe55f5MVJzk18pG7_QWhucmISIW6ra8tqnVVKgpbjiVcJDUSlCG0rO7BUBRoYa6Y3XfGVcz-jZBOyPScYKBAHzSoasgG-n_pHROMv7TvCzhsmMLidmg5OjqIYsxv5O2azt2X9zsGz5ERkT-BBquhOzZSiTCDGyWEnULvAKGA8Dqtaw7BQY3muWORcTXgTX9TiX8JngWw_wvZp1p5GlZf8m8=w281-h72-no)

To display list of the tables avaliable in database run `\dt`

![](https://lh3.googleusercontent.com/QuUsMuZsxNjCpw3GLFbRVJcyXOkreEpNL92ioTWY4snau6tO4rN_lYM5ygN16NuiAfGcqpV1eQe3wIugDqcEpHelJn1BIy4u85xzf0G6Tq-c5kgwYz9qekUJ7wgbDLnJ4C73KNOagOipssrdtAa5W-YYF3x9aJkd0O_e8YXRIko7-d7YHJpa-BN6i89NCz-e5zSO2lel9erCPP7OKG72g48A4q2owobA2kwTEYOW64w2oTTth8ku7N9twE0ocA1pKWCjewmRiPmA3muKRa8RVeIZfm7ZGsM58x5mpRPINlbD-9EejRNMZoVztWXgNIbv0IbU_tgCynPKJA9IK5ub65ROFT2Y7Od1hyYxEaElflMjCphGg1VRsfWc-Y9kxzZgX7j4M9XKSmk7np-NAy2Z1ycw87p-3edvEN39KpWOFUhN6S_WzMJh8DrTUF4SzyoMtASgHXuCVvZ0lq1hZ76Fr7sUib1Zo7TORbZw6QFzwPQLDJQpnKBVEKgTZxwqaCxjrc1ZkFa0tvA8jolebuDZpgOsFfqpWSBudauiBYCjEetP69oditHgSliM-ZekCPRI3_w19iTgoz5Ad7G_PduFIYmsqnaSuBKVcSvnN8Q=w294-h122-no)

The news database includes three tables:
- The `authors` table includes information about the authors of articles.
- The `articles` table includes the articles themselves.
- The `log` table includes one entry for each time a user has accessed the site.

### Create views
Inside newsdatabase you need to create the following views:
```sql
    create view top_view_art as select author, count(*)
    as views from articles join log
    on log.path = concat('/article/', articles.slug)
    group by articles.author order by views desc;
```
```sql
    create view total_request as select time::timestamp::date
    as date, count(*) as total_req  from
    log group by date order by total_req desc;
```
```sql
    create view total_bad_request as select time::timestamp::date 
    as date, count(*) as bad_req from log
    where status='404 NOT FOUND'
    group by date order by bad_req desc;
```

## Run the program
Inside your Virtual machine run `python logAnalysis.Project.py`

![](https://lh3.googleusercontent.com/HZ_xybar2K-HBEao0vhPAt679ZNmDDDp0e24PMWcmCGQfxoOQP-l4LO7X5NPKzRf19lHurWgUw4Dx_tHhGZlHhDKnv8Jzi3qXBwUNBkfmIesSNY4nz78ElvlqxK6L1ORsCzQ0XTOCgg7hOZyDliazlt-9cJY6w0c9T7ZbdQtyY70Uaw5CbhVzfhVxo9ZvjrmZevwoq3ZtW5hn5E8srzVpn2ZFoO4MmlG40lApFQpT0_z2_7FNOv0MvvktwEPU315RzCDpMqlghEDsSQ_ezaf3-YM9lZBXVRnenz3CizBBd0ZfQ0Nz8h9QeBMWFzmlMXzq21k3VZC0WvAljKNUbn19fKaAPtszSO-jk82AziMx-_cb3tYADp_eqLa7ngcEaug60m9DbwrwC9RGZtESS0DmUpDlp3oHtTU8VR8mLLCM09mzb8QF74APVqBJpk-VSsiVKQgn1mDYC_VSsLhIOkWIFexV9V-zRoX0YDUlZ0mC1q28OmZHFguFIaIvPWHQkHMmlhLt-dr9bjSBLKS5sxEAijdKbNFxgQmmVMt6nWrq_uX_vBmNlvmhNzfWNLASxDKvzbSY2oW2iS4bap12O08HF68ye6udHyyWxxFPzc=w400-h40-no)

and read all the answers!

