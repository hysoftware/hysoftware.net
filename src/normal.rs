use ::dioxus::prelude::*;

use crate::sns::SNS;

#[component]
pub fn Normal() -> Element {
  return rsx! {
    section {
      class: "normal",
      header {
        h1 { "Hiroaki Yamamoto" }
      }
      p { "Coder / Hacker / Software and Web Engineer / Translator / etc..." }
      SNS {},
    }
  };
}
