use ::dioxus::prelude::*;

use super::ctrl::Ctrl;

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
          a {
            href: link.href(),
            target: "_blank",
            class: "sns-link btn btn-light",
            i {
              "class": link.icon(),
            }
            "{link.text()}"
          }
        }
      })
    }
  };
}
