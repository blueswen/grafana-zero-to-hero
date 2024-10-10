// dashboard.libsonnet
local g = import 'github.com/grafana/grafonnet/gen/grafonnet-latest/main.libsonnet';
local dashboard_name = "Jsonnet Dashboard";
local text_content = "# Hello, Jsonnet!";

g.dashboard.new(dashboard_name) 
+ g.dashboard.withUid('jsonnet-dashboard')
+ g.dashboard.withDescription('Demo dashboard as code with jsonnet')
+ g.dashboard.withPanels([
    g.panel.text.new("Text Panel")
    + g.panel.text.options.withMode('markdown')
    + g.panel.text.options.withContent(text_content)
    + g.panel.text.panelOptions.withGridPos(h=8, w=24, x=0, y=0)
])
