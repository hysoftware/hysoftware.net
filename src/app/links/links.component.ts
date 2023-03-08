import { Component } from '@angular/core';
import { IconDefinition } from '@fortawesome/fontawesome-svg-core';
import { faFileCode, faFilePdf } from '@fortawesome/free-solid-svg-icons';
import { faGithub, faGitlab, faKeybase } from '@fortawesome/free-brands-svg-icons';

interface Link {
  icon: IconDefinition;
  link: string;
  name: string;
}

@Component({
  selector: 'app-links',
  styleUrls: ['./links.component.scss'],
  templateUrl: './links.component.html',
})
export class LinksComponent {

  public misc: Link[] = [
    {
      icon: faFileCode,
      link: 'https://github.com/hysoftware/hysoftware.net',
      name: 'Code of This Page'
    },
    {
      icon: faFilePdf,
      link: 'https://www.canva.com/design/DADks8eRENo/4npkcNMd5b5OSyFNTXXMvw/view',
      name: 'Resume about me'
    }
  ];
  public snsList: Link[] = [
    {
      icon: faGithub,
      link: 'https://github.com/hiroaki-yamamoto',
      name: 'Github',
    },
    {
      icon: faGitlab,
      link: 'https://gitlab.com/hiroaki-yamamoto',
      name: 'Gitlab',
    },
    {
      icon: faKeybase,
      link: 'https://keybase.io/hyamamoto',
      name: 'Keybase'
    }
  ];

  constructor() { }

}
