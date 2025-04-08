use crate::icon::Icons;

#[derive(Debug, Eq, PartialEq)]
pub struct Link {
  icon: Option<Icons>,
  href: String,
  text: String,
  target: String,
}

impl Link {
  pub fn new(
    icon: Option<Icons>,
    href: &str,
    target: &str,
    text: &str,
  ) -> Self {
    return Self {
      icon,
      href: href.into(),
      target: target.into(),
      text: text.into(),
    };
  }
  pub fn target(&self) -> &str {
    return &self.target;
  }
  pub fn icon(&self) -> &Option<Icons> {
    return &self.icon;
  }
  pub fn href(&self) -> &str {
    return &self.href;
  }
  pub fn text(&self) -> &str {
    return &self.text;
  }
}
