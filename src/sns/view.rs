use ::dioxus::prelude::*;

use super::ctrl::Ctrl;
use crate::links::ButtonLink;

#[component]
pub fn SNS() -> Element {
  let ctrl = use_signal(|| Ctrl::new());
  return rsx! {
    section {
      header {
        h2 { "SNS" }
      }
    }
    {
      ctrl.read().links().iter().map(|link| {
        rsx!{
          ButtonLink {
            a_class: "btn btn-light btn-lg",
            link: link.clone(),
          }
        }
      })
    }
  };
}
