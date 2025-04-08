use ::std::sync::Arc;

use ::dioxus::prelude::*;

use crate::icon::Icon;

use super::super::entities::Link;

#[component]
pub fn ButtonLink(a_class: String, link: Arc<Link>) -> Element {
  return rsx! {
    a {
      class: "link-btn {a_class}",
      href: link.href(),
      target: link.target(),
      div {
        class: "link-label",
        if let Some(icon) = link.icon() {
          Icon { icon: icon.clone() }
        }
        "{link.text()}",
      }
    },
  };
}
