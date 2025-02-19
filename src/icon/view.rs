use dioxus::prelude::*;

use super::fontawesome::{GITHUB, GITLAB, KEYBASE};
use super::icons::Icons;

#[component]
pub fn Icon(icon: Icons) -> Element {
  return rsx! {
    div {
      class: "icon",
      dangerous_inner_html: {
        match icon {
            Icons::FaGithub => GITHUB,
            Icons::FaGitlab => GITLAB,
            Icons::FaKeybase => KEYBASE,
        }
      }
    }
  };
}
