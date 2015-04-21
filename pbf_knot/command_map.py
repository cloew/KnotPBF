from pbf.Commands.command_manager import CommandConfig, RegisterCommands

commands = [CommandConfig("new knot-pkg", "pbf_knot.Commands.new_knot_pkg.NewKnotPkg", description="Create a new Knot Package config"),
            CommandConfig("mk knot-pkg", "pbf_knot.Commands.mk_knot_pkg.MkKnotPkg", description="Make a new Knot Package"),
            CommandConfig("new knot-app", "pbf_knot.Commands.new_knot_app.NewKnotApp", description="Create a new Knot App config")]

RegisterCommands(commands)