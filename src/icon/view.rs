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

#[cfg(test)]
mod tests {
  use super::{Icon, IconProps};
  use crate::icon::fontawesome::{GITHUB, GITLAB, KEYBASE};
  use crate::icon::icons::Icons;
  use dioxus::prelude::*;
  use pretty_assertions::assert_eq;

  #[test]
  fn test_icon_github() {
    let icon = dioxus_ssr::render_element(Icon(IconProps {
      icon: Icons::FaGithub,
    }));
    let correct = dioxus_ssr::render_element(rsx! {
      div {
        class: "icon",
        dangerous_inner_html: GITHUB,
      }
    });
    assert_eq!(icon, correct);
  }

  #[test]
  fn test_icon_gitlab() {
    let icon = dioxus_ssr::render_element(Icon(IconProps {
      icon: Icons::FaGitlab,
    }));
    let correct = dioxus_ssr::render_element(rsx! {
      div {
        class: "icon",
        dangerous_inner_html: GITLAB,
      }
    });
    assert_eq!(icon, correct);
  }

  #[test]
  fn test_icon_keybase() {
    let icon = dioxus_ssr::render_element(Icon(IconProps {
      icon: Icons::FaKeybase,
    }));
    let correct = dioxus_ssr::render_element(rsx! {
      div {
        class: "icon",
        dangerous_inner_html: KEYBASE,
      }
    });
    assert_eq!(icon, correct);
  }
}
