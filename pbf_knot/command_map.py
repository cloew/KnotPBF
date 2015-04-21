from pbf.Commands.command_manager import CommandConfig, RegisterCommands

commands = [CommandConfig("new knot-pkg", "pbf_knot.Commands.new_knot_pkg.NewKnotPkg", description="Create a new Knot Package")]

RegisterCommands(commands)