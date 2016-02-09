g = require "gulp"
notify = require "gulp-notify"
childProcess = require "child_process"
q = require "q"

g.task "check.backend", ->
  testCommand = [
    "nosetests"
    "--with-coverage"
    "--cover-erase"
    "--cover-package=app"
    "--all"
  ]
  commands = [
    "echo 'PEP8 Syntax...'"
    "flake8 app"
    "echo 'Code Metrics...'"
    "radon cc -nc app"
    "echo 'Maintenancibility...'"
    "radon mi -nc app"
    "echo 'Unit testing...'"
    "export secret=\"test\""
    testCommand.join " "
    "unset secret"
  ]
  if not process.env.CI
    commands.splice 0, 0, ". ../bin/activate"
    commands.push "deactivate"
  commands = commands.join ("&&")
  defer = q.defer()
  child = childProcess.exec commands
  child.stdout.pipe process.stdout
  child.stderr.pipe process.stderr
  child.on "error", (error) ->
    notify.onError("<%= error.message %>")(error)
    defer.reject(error)
  child.on "close", (code, signal) ->
    errStr = "The command failed with "
    if code isnt null and code > 0
      codeErr = errStr + " code: #{code}"
      notify.onError("<%= error.message %>")(new Error codeErr)
      defer.reject codeErr
      return
    if signal isnt null
      codeErr = errStr + " signal: #{signal}"
      notify.onError("<%= error.message %>")(new Error codeErr)
      defer.reject codeErr
      return
    defer.resolve()
  defer.promise
