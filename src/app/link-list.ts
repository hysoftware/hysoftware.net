import { Injectable } from '@angular/core';
import { IconDefinition } from '@fortawesome/angular-fontawesome';
import { faFileCode, faFile } from '@fortawesome/free-solid-svg-icons';
import { faGithub, faGitlab, faKeybase } from '@fortawesome/free-brands-svg-icons';

interface Link {
  icon: IconDefinition;
  link: string;
  name: string;
}

@Injectable({
  providedIn: 'root',
})
export class LinkList {
  public readonly snsList: Link[] = [
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
  public readonly miscList: Link[] = [
    {
      icon: faFileCode,
      link: 'https://github.com/hysoftware/hysoftware.net',
      name: 'Code of This Page'
    },
    {
      icon: faFile,
      link: 'https://www.canva.com/design/DADks8eRENo/4npkcNMd5b5OSyFNTXXMvw/view',
      name: 'Resume about me'
    },
  ];
}
