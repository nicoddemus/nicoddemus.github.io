Title: clik: framework for command-line applications
Date: 2013-08-25 22:03
Category: Python
tags: command-line, python, script
Summary: Quick overview of a command-line application framework

While working on [cit](https://github.com/nicoddemus/cit), I decided that subcommand 
handling that was being done manually was too clumsy (specially after 
[Damiani](https://github.com/damianimc) went on a flurry and added a ton of new commands). 
That's when I found out about this neat little
framework for subcommand-style applications: [clik](https://github.com/jds/clik).

You initially must construct an `App` object:

``` python
cit = clik.App(
    name='cit',
    description='Command line tool for interacting with a Jenkins integration server.\n', 
) 

...

if __name__ == '__main__':
    cit.main()    
```

Now with an app object on hand, you can use it as a decorator in any function you have, 
which then exposes that function in the command line as a subcommand of your application:

``` python
@cit(alias='fb.add', usage='[branch]')
def feature_branch_add(...):
     '''
    Create/Update jobs associated with the current git branch.
    
    This will create one or more jobs on jenkins for the current feature branch,
    or for the one given as parameter if one is provided.
    '''    
```

By default the sub-command is named after the function itself, but you can pass an alias if you like
(`feature_branch_add` is too long to type in the command line). The docstring is also parsed and
the first line is used as a "short help", while the rest is displayed when asking for more
detailed help for a command:

```bash 
$ cit
cit -- Command line tool for interacting with a Jenkins integration server.

Basic usage: cit <subcommand> [options]

feature_branch_add, fb.add
    Create/Update jobs associated with the current git branch.

$ cit fb.add -h
Usage: cit feature_branch_add|fb.add [branch]

Create/Update jobs associated with the current git branch.

Options:
  -h, --help  show this help message and exit

This will create one or more jobs on jenkins for the current feature branch,
or for the one given as parameter if one is provided.
```

Neat stuff!

Your subcommands may receive some predefined arguments, all you have to do is to declare
the argument by name and `clik` will automatically inspect the function and pass
the correct parameters:

* `args`: List of arguments, not including application or command name.
* `argv`: List of arguments including the command name.
* `opts`: optparse.Values for the invocation.
* `app`: The click.App running the subcommand.
* `console`: clik.Console object.
* `conf`: ConfigParser.ConfigParser instance. Will be empty if conf is not enabled.
* `log`: logging.Logger instance for the application. Has no handlers (thus does "nothing") if logging is not enabled.

There's some really handy features available, like colored output, configuration handling, etc.
You can also customize the parameters. In cit's case I added a few more parameters that 
subcommands can receive:

* `job_config`: job configuration for the current repository.
* `global_config`: global cit configuration.
* `user_name`: current git user name.
* `user_email`: current git user email. 
* `branch` : current git branch.

Here's `fb.rm` making use of the custom parameters:

``` python
@cit(alias='fb.rm', usage='[branch]')
def feature_branch_rm(branch, global_config):
    '''
    Remove jobs associated with the current git branch.
    '''
```

All in all, `clik` is a neat little library that greatly helps having to write a lot of 
boilerplate code for command line handling. Highly recommended!

**Note**: the above code is in a branch `better-command-line-handling`... it will
be integrated in `master` this week (I think).

