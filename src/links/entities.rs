use crate::icon::Icons;

#[derive(Debug)]
pub struct Link {
  icon: Option<Icons>,
  href: String,
  text: String,
}

impl Link {
  pub fn new(icon: Option<Icons>, href: &str, text: &str) -> Self {
    return Self {
      icon,
      href: href.into(),
      text: text.into(),
    };
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
