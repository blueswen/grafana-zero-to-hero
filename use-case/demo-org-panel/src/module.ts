import { PanelPlugin } from '@grafana/data';
import { OrganizationPanelOptions } from './types';
import { SimplePanel } from './components/SimplePanel';

// export const plugin = new PanelPlugin(SimplePanel);

export const plugin = new PanelPlugin<OrganizationPanelOptions>(SimplePanel).setPanelOptions((builder) => {
  builder.addRadio({
    path: 'displayMode',
    name: 'Display mode',
    settings: {
      options: [
        { value: 'select', label: 'Select', description: 'A searchable dropdown menu' },
        { value: 'button', label: 'Button', description: 'Individual buttons' },
      ],
    },
    defaultValue: 'select',
  });
  return builder;
});


// export const plugin = new PanelPlugin<OrganizationPanelOptions>(SimplePanel).setPanelOptions((builder) => {
//   return builder();
// });

// export const plugin = new PanelPlugin<SimpleOptions>(SimplePanel).setPanelOptions((builder) => {
//   return builder
//     .addTextInput({
//       path: 'text',
//       name: 'Simple text option',
//       description: 'Description of panel option',
//       defaultValue: 'Default value of text input option',
//     })
//     .addBooleanSwitch({
//       path: 'showSeriesCount',
//       name: 'Show series counter',
//       defaultValue: false,
//     })
//     .addRadio({
//       path: 'seriesCountSize',
//       defaultValue: 'sm',
//       name: 'Series counter size',
//       settings: {
//         options: [
//           {
//             value: 'sm',
//             label: 'Small',
//           },
//           {
//             value: 'md',
//             label: 'Medium',
//           },
//           {
//             value: 'lg',
//             label: 'Large',
//           },
//         ],
//       },
//       showIf: (config) => config.showSeriesCount,
//     });
// });
