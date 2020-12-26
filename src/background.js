"use strict";
const {contextMenus, i18n, runtime} = browser;
contextMenus.create({
  title: i18n.getMessage("contextMenuItemTitle"),
  contexts: ["selection"]
});
contextMenus.onClicked.addListener(({selectionText}) => {
  runtime.sendNativeMessage(
    "gnome_dictionary_lookup",
    `--look-up=${selectionText}`
  ).then(
    null,
    (error) => {
      console.log(error);
    }
  );
});
