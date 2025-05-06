# Setup

Video on snowflake and snowsql setup :point_down:

> [!Note]
> Videos for snowflake lectures come from another course, so we are sometimes referring to another course in the videos. But the contents can be used directly for this current course.

[![setup snowflake](https://github.com/kokchun/assets/blob/main/data_warehouse/setup_snowflake_video.png?raw=true)](https://www.youtube.com/watch?v=i454nHjdMAc)


## Snowflake account

Now we will create a [snowflake free trial account](https://signup.snowflake.com/), which can be used for 30 days, with $400 credits.

> [!NOTE]
> Pick enterprise version.

<img width = "400" src="https://github.com/kokchun/assets/blob/025ae8622a25d5522d11b21108f52f1df9388ea2/data_warehouse/snowflake_free_trial.png?raw=true"/>

<!-- TODO: navigation of snowsight -->

## SnowSQL setup

SnowSQL is a CLI tool for snowflake which we will be using. The reason for us to use this is to version control our SQL scripts using git and github, and also to have everything in one place in our repository.

Go into [this page](https://developers.snowflake.com/snowsql/) and find your operating system for installing snowsql.

<details> <summary> <b>Windows installation</b></summary>

After you've installed snowsql for windows, go into git bash and try out the following command

```bash
snowsql -v
```

It works if you get back a version number. Also try

```bash
snowsql
```

to see some of the options. Now navigate to the .snowsql directory, it should be installed here `/c/Users/<your_user>/.snowsql`. You can navigate there using `cd` and then do

```bash
code config
```

if you have configured the `code` before. Otherwise just open it in notepad using

```bash
notepad config
```

</details>

</br>

<details> 
<summary> <b>Mac installation</b></summary>
    
Either use the isntallation package provided above or use homebrew.

If using homebrew type in this command in mac terminal

```bash
brew install --cask snowflake-snowsql
```

Try the command in mac terminal

```bash
snowsql -v
```

It works if you get back a version number. Also try

```bash
snowsql
```

If it doesn't work you need to configure an alias to snowsql

1. Open (or create, if missing) the ~/.zshrc file.

2. Add the following line:

```bash
alias snowsql=/Applications/SnowSQL.app/Contents/MacOS/snowsql
```

3. Save the file.

4. Retry the commands above to see if snowsql is working.

Now go into your terminal and navigate to `.snowsql` folder

```bash
cd ~/.snowsql
```

Open config file with `code config` if you have `code` configured on your mac otherwise use `open config` to open it in a text editor.

</details>

### config file

Inside config file fill in

```yaml
[connections.dwh_course] # before this was [connections.example]
accountname =
username =
password =
warehousename = COMPUTE_WH
```

> [!NOTE]
> move on to accountname section to find accountname
> move on to username section to find username

move on to accountname section

### accountname

To find your user account follow these steps

1. on the sign in page of snowflake, you can find the url similar to the pattern below on the browser:

```bash
https://<account_identifier>.<region>.azure.snowflakecomputing.com
```

2. paste this into user account in .snowsql, but keep only the part that is `<account_identifier>.<region>.azure`

### username

In snowflake go into `admin` and then `users & roles` to find your user.

### Snowflake extension

Now install snowflake extension on vscode by searching for snowflake or use this link: [snowflake extension for vscode](https://marketplace.visualstudio.com/items?itemName=snowflake.snowflake-vsc).

Log into your snowflake account using account_url, username and password

### Snowsql config path

Go into settings in your vscode with `ctrl+shift+p` or `cmd+shift+p`, then type and click on

```
Preferences: Open User Settings
```

Now type in `snowsql` and paste in the path to your snowsql config file. You can find the path through navigating to .snowsql directory and type

```bash
pwd 
```

then add "/config" to the ending of that path. 

> [!IMPORTANT]
> If you are on **windows**, you might get `c:/Users/...` from `pwd`.
>  
> Make sure to remove `c:` so the final path could be something like `/Users/aigineer/.snowsql/config` 

## Create a github repository

Now we will create a github repository online, then clone it, so that you can work with it locally. Name your github repository as follows and make it public

```
data_warehouse_<first_name>_<last_name>_<class>
```

> [!IMPORTANT]
> Add the python .gitignore to your repository in order to not track certain files in version control.

Clone the repository to a local directory of your choice, e.g. `documents/github`.

Now create the following directories to organize your files: 

- exercises 
- code-alongs
- explorations

## Test snowsql

Navigate to your repository and create a file called `test_snowsql.sql` and add a few statements 

```sql
SHOW databases;

USE SCHEMA snowflake_sample_data.tpch_sf1;

SHOW TABLES;

SELECT * FROM CUSTOMER;
```

Make sure to have logged in to snowflake through its vscode extension. 

> [!NOTE]
> You might need to change the language mode to snowflake SQL if it isn't set by defa

> [!NOTE]
> Use ctrl+enter or cmd+enter to run each sql statements through snowflake.


## Other videos :video_camera:

- [How to use SnowSQL | Install, Config & Query - Kahan Data Solutions (2023)](https://www.youtube.com/watch?v=ogg9SLBRZ9A)


## Read more :eyeglasses:

- [install snowsql](https://docs.snowflake.com/en/user-guide/snowsql-install-config)  
- [configure snowsql](https://docs.snowflake.com/en/user-guide/snowsql-config)